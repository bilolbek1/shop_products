from django import forms
from .models import Shop, Product, Category


#############------------THIS FORM IS FOR EDIT OR ADD PRODUCTS---------##############
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'amount', 'category', 'shop', 'product_image', 'description']


#############------------THIS FORM IS FOR SHOP DATA---------##############
class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = "__all__"


#############------------THIS FORM IS FOR CATEGORY DATA---------##############
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
