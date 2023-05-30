from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from product.models import Product


class ProductListView(ListView):
    model = Product
    # 'product_list.html', {'product_list': Product.objects.all()}
    paginate_by = 3


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price']  # '__all__'
    template_name_suffix = '_create'  # product_form.html -> product_create.html
    success_url = reverse_lazy('product:list')  # 만들기 성공하면 이동할 url 이름


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price']  # '__all__'
    template_name_suffix = '_update'
    # success_url = reverse_lazy('product:list')  # 수정 성공하면 이동할 url 이름


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product:list')


def list_product(request):
    product_list = Product.objects.all()  # product 다 가져오자
    context = {'product_list': product_list}
    return render(request, 'product/product_list.html', context)


def detail_product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'product/product_detail.html', context)
