from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),  # URL สำหรับหน้า index
]
