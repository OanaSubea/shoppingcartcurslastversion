from django.shortcuts import render
from .models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'list.html', context)

def category_prodcut_list(request, categoryid = 1 ): # 1 - default
    categories = Category.objects.all()
    products = Product.objects.filter(category=categoryid) #produsele sunt filtrate in functie de categorie - nu listez toate produsele doar cele pentru categoria respectiva
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'categoryproductlist.html', context)
def product_detail(request, productid):
    id = productid
    produs = Product.objects.get(pk=int(id)) #pk= primary key - sa ma duc pe fiecare produs
    print(produs.id)
    cart_product_form = CartAddProductForm()
    context = {
        'produs': produs,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'produs.html', context)