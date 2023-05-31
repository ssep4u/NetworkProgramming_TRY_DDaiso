from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from product.forms import ProductCreationForm, ProductChangeForm
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


def create_product(request):
    if request.method == 'POST':  # 사용자가 입력하고 버튼 눌렀을 때
        form = ProductCreationForm(request.POST)  # form 가져오자
        if form.is_valid():
            form.save()  # new_product 저장하자
        return redirect('product:list2')
    else:  # 빈 폼
        form = ProductCreationForm()
    return render(request, 'product/product_create.html', {'form': form})


def update_product(request, pk):
    if request.method == 'POST':  # 사용자가 입력하고 버튼 눌렀을 때
        form = ProductChangeForm(request.POST)  # form 가져오자
        if form.is_valid():
            product = Product.objects.get(pk=pk)  # pk에 해당하는 product 가져오자
            product.name = form.cleaned_data.get('name')  # 사용자가 입력한 name set
            product.price = form.cleaned_data.get('price')  # 사용자가 입력한 price set
            product.save()  # 수정한 product 저장하자
        return redirect('product:list2')
    else:
        product = Product.objects.get(pk=pk)
        form = ProductChangeForm(instance=product)
    return render(request, 'product/product_update.html', {'form': form})


def delete_product(request, pk):
    if request.method == 'POST':  # 사용자가 입력하고 버튼 눌렀을 때
        product = Product.objects.get(pk=pk)  # pk에 해당하는 product 가져오자
        product.delete()  # product 삭제하자
        return redirect('product:list2')
    else:
        product = Product.objects.get(pk=pk)
    return render(request, 'product/product_confirm_delete.html', {'product': product})
