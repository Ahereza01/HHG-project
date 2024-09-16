from django.forms import ModelForm
from .models import *

class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity','amount_received','issued_to']
#we are transferring the model where it will sit

class AddForm(ModelForm):
    class Meta:
        model = Stockx
        fields = ['total_quantity'] #his form is based on the stock model.