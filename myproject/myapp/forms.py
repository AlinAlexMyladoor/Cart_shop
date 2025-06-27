from django import forms
from .models import *


class RegiterForm(forms.ModelForm):
    
    class Meta:
        model = Register
        fields = ['first_name','last_name','username','email','password','contact']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class EditForm(forms.ModelForm):
    
    class Meta:
        model = Register
        fields = ['first_name','last_name','username','email','contact']
        help_text = {
            'username': None
        }

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'image']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(forms.ModelForm):
    price = forms.DecimalField(
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': '1',
            'step': '0.01',
            'placeholder': 'Enter price'
        })
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'image']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        
        self.fields['category'].queryset = Category.objects.all()

  