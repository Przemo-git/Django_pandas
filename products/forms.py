from django import forms
from .models import Purchase, Product

class PurchaseForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(),    ####kolejność qlw
                                         label='Product',
                                         widget=forms.Select(attrs={'class': 'ui selection field'}))
                                        #tutaj odwołanie do stylowania w css .field-with...
    class Meta:
        model = Purchase
        fields = ['product', 'price', 'quantity']





class ProductForm(forms.ModelForm):


    class Meta:
        model = Product
        fields = ('name',)






