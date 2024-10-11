from django.urls import path
from .views import index, order_page, remove_from_cart, confirm_delete, add_to_cart, cart_page, CheckoutView, success_page

urlpatterns = [
    path('', index, name='index'),  # หน้าแสดงผลิตภัณฑ์ทั้งหมด
    path('order/<str:order_number>/', order_page, name='order_page'),  # หน้าเพื่อสั่งซื้อสินค้า
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),  # ฟังก์ชันลบสินค้าออกจากรถเข็น
    path('cart/confirm_delete/<int:product_id>/', confirm_delete, name='confirm_delete'),  # ยืนยันการลบสินค้า
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),  # ฟังก์ชันเพิ่มสินค้าลงในรถเข็น
    path('cart/', cart_page, name='cart_page'),  # หน้าแสดงสินค้าที่อยู่ในรถเข็น
    path('checkout/', CheckoutView.as_view(), name='checkout_page'),  # หน้าชำระเงิน
    path('success/', success_page, name='success_page'),
]
