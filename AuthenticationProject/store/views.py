from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order
from .forms import OrderForm
from django.contrib import messages
from decimal import Decimal
from django.views import View
from django.views import View  # ต้องแน่ใจว่ามีการ import View

# หน้าหลัก แสดงผลิตภัณฑ์ทั้งหมด
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

# หน้าสำหรับสั่งซื้อสินค้า
def order_page(request, order_number=None):
    if order_number is None:
        return redirect('cart_page')

    try:
        product = Product.objects.get(order_number=order_number)
    except Product.DoesNotExist:
        return redirect('cart_page')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_success')
    else:
        form = OrderForm()

    return render(request, 'order_page.html', {
        'form': form,
        'product': product
    })

# ฟังก์ชันลบสินค้าออกจากรถเข็น
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
        messages.success(request, 'Product removed from cart successfully.')
    else:
        messages.error(request, 'Product not found in cart.')

    return redirect('cart_page')

# ฟังก์ชันยืนยันการลบสินค้า
def confirm_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        if str(product_id) in cart:
            del cart[str(product_id)]
            request.session['cart'] = cart
            messages.success(request, 'Product removed from cart successfully.')
        else:
            messages.error(request, 'Product not found in cart.')

        return redirect('cart_page')

    return render(request, 'confirm_delete.html', {'product': product})

# ฟังก์ชันเพิ่มสินค้าลงในรถเข็น
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': str(product.price),
            'quantity': 1,
            'image_url': product.image_url
        }

    request.session['cart'] = cart
    return redirect('cart_page')

# หน้าแสดงสินค้าที่อยู่ในรถเข็น
def cart_page(request):
    cart = request.session.get('cart', {})
    total = sum(float(item['price']) * item['quantity'] for item in cart.values())
    return render(request, 'cart_page.html', {'cart': cart, 'total': total})

# หน้าชำระเงิน
class CheckoutView(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        cart_items = []
        total_price = Decimal('0.00')

        for product_id, item in cart.items():
            product = get_object_or_404(Product, id=product_id)
            item_total = product.price * item['quantity']
            total_price += item_total

            cart_items.append({
                'name': product.name,
                'price': product.price,
                'quantity': item['quantity'],
                'total': item_total,
                'image_url': item['image_url'],
            })

        shipping_fee = Decimal('100.00')
        final_total = total_price + shipping_fee

        form = OrderForm()  # สร้างฟอร์มใหม่
        context = {
            'cart_items': cart_items,
            'total_price': total_price,
            'shipping_fee': shipping_fee,
            'final_total': final_total,
            'form': form,  # เพิ่มฟอร์มใน context
        }
        return render(request, 'checkout_page.html', context)

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()  # บันทึกคำสั่งซื้อ
            return redirect('success_page')  # เปลี่ยนเส้นทางไปยังหน้า success_page
        # ถ้าฟอร์มไม่ถูกต้อง ให้แสดงหน้าฟอร์มอีกครั้ง
        cart = request.session.get('cart', {})
        cart_items = []
        total_price = Decimal('0.00')

        for product_id, item in cart.items():
            product = get_object_or_404(Product, id=product_id)
            item_total = product.price * item['quantity']
            total_price += item_total

            cart_items.append({
                'name': product.name,
                'price': product.price,
                'quantity': item['quantity'],
                'total': item_total,
                'image_url': item['image_url'],
            })

        shipping_fee = Decimal('100.00')
        final_total = total_price + shipping_fee

        context = {
            'cart_items': cart_items,
            'total_price': total_price,
            'shipping_fee': shipping_fee,
            'final_total': final_total,
            'form': form,  # ส่งฟอร์มกลับไปพร้อมข้อความแสดงข้อผิดพลาด
        }
        return render(request, 'checkout_page.html', context)

def success_page(request):
    return render(request, 'success_page.html')  # สร้างเทมเพลต success_page.html