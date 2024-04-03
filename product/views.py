from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View

from .forms import ProductForm, ShopForm, CategoryForm
from .models import Category, Product, Shop


#############------------THIS VIEW IS FOR SHOPS PAGE AND THERE ARE SHOPS LIST---------##############
class ShopPageView(View):
    def get(self, request):
        shops = Shop.objects.order_by('-id')
        search = request.GET.get('search', '')
        if search:
            shops = shops.filter(
                Q(title__icontains=search)
            )
        context = {
            'shops': shops
        }
        return render(request, 'shop.html', context)


#############------------THIS VIEW IS FOR PRODUCTS PAGE AND THERE ARE PRODUCTS LIST
# AND SEARCHING---------##############
class ProductPageView(View):
    def get(self, request):
        categories = Category.objects.all()
        products = Product.objects.order_by('-id')
        search = request.GET.get('search', '')
        print(search, type(search))
        if search:
            products = products.filter(
                Q(title__icontains=search) or Q(category__name__icontains=search)
            )
        context = {
            'products': products,
            'categories': categories,
        }
        return render(request, 'product.html', context)


#############------------THIS VIEW IS FOR FILTERED PRODUCTS BY PRICE---------##############
class FilterProductView(View):
    def post(self, request):
        products = Product.objects.order_by('-price')
        categories = Category.objects.all()
        context = {
            'products': products,
            'categories': categories
        }
        return render(request, 'product.html', context)


#############------------THIS VIEW IS FOR CATEGORY PAGE---------##############
class CategoryPageView(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'category.html', context)


#############------------THIS VIEW IS FOR ADD PRODUCT---------##############
class AddProductView(View):
    def get(self, request):
        add_product_form = ProductForm()
        context = {
            'add_product_form': add_product_form,
        }
        return render(request, 'add_product.html', context)

    def post(self, request):
        add_product_form = ProductForm(data=request.POST, files=request.FILES)
        if add_product_form.is_valid():
            Product.objects.create(
                title=add_product_form.cleaned_data['title'],
                price=add_product_form.cleaned_data['price'],
                amount=add_product_form.cleaned_data['amount'],
                category=add_product_form.cleaned_data['category'],
                shop=add_product_form.cleaned_data['shop'],
                product_image=add_product_form.cleaned_data['product_image'],
                description=add_product_form.cleaned_data['description']
            )
            return redirect('product_page')

        else:
            context = {
                'add_product_form': add_product_form,
            }
            return render(request, 'add_product.html', context)


#############------------THIS VIEW IS FOR EDIT PRODUCTS DATA---------##############
class EditProductView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        edit_product_form = ProductForm(instance=product)
        context = {
            'edit_product_form': edit_product_form
        }
        return render(request, 'edit_product.html', context)

    def post(self, request, id):
        product = Product.objects.get(id=id)
        edit_product_form = ProductForm(instance=product, data=request.POST, files=request.FILES)
        if edit_product_form.is_valid():
            edit_product_form.save()

            return redirect('product_page')

        else:
            context = {
                'edit_product_form': edit_product_form
            }
            return render(request, 'edit_product.html', context)


#############------------THIS VIEW IS FOR GET PRODUCTS WITH CATEGORY---------##############
class CategoryProductPageView(View):
    def get(self, request, category_name):
        categories = Category.objects.all()
        products = Product.objects.filter(category__name=category_name)
        context = {
            'products': products,
            'categories': categories,
        }
        return render(request, 'category_product.html', context)


#############------------THIS VIEW IS FOR EDIT SHOPS DATA---------##############
class EditShopView(View):
    def get(self, request, id):
        shop = Shop.objects.get(id=id)
        edit_shop_form = ShopForm(instance=shop)
        context = {
            'edit_shop_form': edit_shop_form
        }
        return render(request, 'edit_shop.html', context)

    def post(self, request, id):
        shop = Shop.objects.get(id=id)
        edit_shop_form = ShopForm(instance=shop, data=request.POST, files=request.FILES)
        if edit_shop_form.is_valid():
            edit_shop_form.save()

            return redirect('shop_page')

        else:
            context = {
                'edit_shop_form': edit_shop_form
            }
            return render(request, 'edit_shop.html', context)


#############------------THIS VIEW IS FOR ADD CATEGORY---------##############
class AddCategoryView(View):
    def get(self, request):
        category_form = CategoryForm()
        context = {
            "category_form": category_form
        }
        return render(request, 'add_category.html', context)

    def post(self, request):
        category_form = CategoryForm(data=request.POST)
        if category_form.is_valid():
            category_form.save()

            return redirect('category_page')
        else:
            context = {
                "category_form": category_form
            }
            return render(request, 'add_category.html', context)
