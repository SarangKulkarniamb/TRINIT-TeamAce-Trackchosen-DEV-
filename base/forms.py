from django.forms import ModelForm
from .models import *

class Memberform(ModelForm):
    class Meta:
        model=member
        fields='__all__'

class OrderForm(ModelForm):
    class Meta:
        model=order
        fields='__all__'

class RegisterForm(ModelForm):
    class Meta:
        model=customer
        fields='__all__'
class ProductForm(ModelForm):
    class Meta:
        model=product
        fields='__all__'

