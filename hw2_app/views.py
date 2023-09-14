from django.shortcuts import render
from django.utils import timezone
from django.views.generic import UpdateView
from hw2_app.forms import ProductForm
from hw2_app.models import *


def client_view(request):
    clients = Client.objects.all()
    return render(request, 'hw2_app/clients.html', {'clients': clients})


def product_view(request):
    products = Product.objects.all()
    return render(request, 'hw2_app/products.html', {'products': products, 'title': 'Список товаров'})


def order_view(request):

    if request.GET.get('all_orders'):
        orders = Order.objects.all()
    elif request.GET.get('last_7_days'):
        orders = Order.objects.filter(
            date_order__gte=timezone.now() - timezone.timedelta(days=7))
    elif request.GET.get('last_30_days'):
        orders = Order.objects.filter(
            date_order__gte=timezone.now() - timezone.timedelta(days=30))
    elif request.GET.get('last_365_days'):
        orders = Order.objects.filter(
            date_order__gte=timezone.now() - timezone.timedelta(days=365))
    else:
        orders = Order.objects.all()
    return render(request, 'hw2_app/orders.html', {'orders': orders, 'title': 'Список заказов'})


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'hw2_app/product_edit.html'
    success_url = '/'
