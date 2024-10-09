from django.shortcuts import render, redirect
from .models import Product, Order
from .forms import OrderForm
from django.shortcuts import get_object_or_404

def index(request):
    products = Product.objects.all()  # ดึงผลิตภัณฑ์ทั้งหมด
    return render(request, 'index.html', {'products': products})

def order_page(request):
    # ดึงข้อมูลสินค้าที่ผู้ใช้เลือก
    product = Product.objects.get(id=selected_product_id)  # เปลี่ยน selected_product_id ตามการเลือกสินค้าของคุณ

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # ประมวลผลข้อมูลคำสั่งซื้อ
            form.save()
            return redirect('order_success')
    else:
        form = OrderForm()

    return render(request, 'order_page.html', {
        'form': form,
        'product': product  # ส่งข้อมูลสินค้าทั้งหมดไปยัง Template
    })


def edit_order(request):
    order = Order.objects.first()  # ดึงคำสั่งซื้อตัวแรกหรือเปลี่ยนตามความต้องการ
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_success')  # เปลี่ยนตาม URL
    else:
        form = OrderForm(instance=order)
    return render(request, 'order_page.html', {'form': form})

def delete_order(request):
    order = Order.objects.first()  # ดึงคำสั่งซื้อตัวแรกหรือเปลี่ยนตามความต้องการ
    if request.method == 'POST':
        order.delete()
        return redirect('index')  # เปลี่ยนตาม URL
    return render(request, 'confirm_delete.html', {'order': order})

def order_success(request):
    return render(request, 'order_success.html')
