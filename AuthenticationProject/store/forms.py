from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'address', 'phone', 'payment_method']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter your address here...'}),
        }
        labels = {
            'name': 'Name',
            'address': 'Address',
            'phone': 'Phone Number',
            'payment_method': 'Payment Method',
        }
        help_texts = {
            'name': 'Enter your full name.',
            'address': 'Please provide your complete address.',
            'phone': 'Enter your phone number (e.g., 012-345-6789).',
            'payment_method': 'Specify your preferred payment method (e.g., Credit Card, PayPal).',
        }
