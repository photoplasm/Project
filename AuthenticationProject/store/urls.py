from django.urls import path
from .views import index, order_page, edit_order, delete_order, order_success  # นำเข้าเฉพาะที่ต้องใช้

urlpatterns = [
    path('index/', index, name='index'),  # หน้า index
    path('order/', order_page, name='order_page'),
    path('order/edit/', edit_order, name='edit_order'),  # แก้ไข URL
    path('confirm_delete/', delete_order, name='delete_order'),  # แก้ไข URL
    path('order/success/', order_success, name='order_success'),
]
