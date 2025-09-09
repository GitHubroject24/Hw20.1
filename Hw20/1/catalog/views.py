from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Contact: {name}({phone}): {message}')
    return render(request, 'home.html')

class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    # def contacts(request):
    #     if request.method == 'POST':
    #         name = request.POST.get('name')
    #         phone = request.POST.get('phone')
    #         message = request.POST.get('message')
    #         print(f'Contact: {name}({phone}): {message}')
    #     return render(request, 'catalog/contacts.html')

class ProductListView(ListView):
    model = Product

# def products_list(request):
#     products = Product.objects.all()
#     context = {"products" : products}
#     return render(request, 'products_list.html', context)

class ProductDetailView(DetailView):
    model = Product

# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, 'product_detail.html', context)