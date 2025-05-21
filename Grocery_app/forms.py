from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from .models import Sale,Stockx

class SaleForm(forms.ModelForm):

    quantity = forms.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Quantity'}),
        error_messages={
            'required': 'Quantity is required.',
            'invalid': 'Enter a valid number for quantity.',
            'min_value': 'Quantity must be at least 1.',
            'max_value': 'Quantity cannot exceed 1000.'
        }
    )
    unit_price = forms.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0.01)],
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Unit Price'}),
        error_messages={
            'required': 'Unit price is required.',
            'invalid': 'Enter a valid price.',
            'min_value': 'Unit price must be at least 0.01.'
        }
    )
    amount_received = forms.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0)],
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Amount Received'}),
        error_messages={
            'required': 'Amount received is required.',
            'invalid': 'Enter a valid amount.',
            'min_value': 'Amount received cannot be negative.'
        }
    )
    

    class Meta:
        model = Sale
        fields = ['issued_to', 'quantity', 'unit_price', 'amount_received']

class AddForm(forms.ModelForm):
    class Meta:
        model = Stockx
        fields = ['total_quantity'] #his form is based on the stock model.