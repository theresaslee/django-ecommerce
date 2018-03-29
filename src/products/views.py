# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product


# Create your views here.
class ProductListView(ListView):
    queryset = Product.objects.all()
    # default will be product_list by html, but you can alter
    # template_name = 'products/list.html'

    # same as context dict
    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context

# Same as above
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
    'object_list': queryset
    }
    return render(request, 'products/product_list.html', context)

# Create your views here.
class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    # default will be product_list by html, but you can alter
    # template_name = 'products/list.html'

    # same as context dict
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context

# Same as above
def product_detail_view(request, pk=None):
    instance = get_object_or_404(Product, pk=pk)
    # instance = Product.objects.all(pk=pk) #id
    context = {
    'object': instance
    }
    return render(request, 'products/product_detail.html', context)
