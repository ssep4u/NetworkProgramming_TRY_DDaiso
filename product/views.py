from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from product.forms import ProductCreationForm, ProductChangeForm, ReviewCreationForm, ReviewChangeForm
from product.models import Product, Review


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
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product/product_detail.html', context)


def create_product(request):
    if request.method == 'POST':  # 사용자가 입력하고 버튼 눌렀을 때
        form = ProductCreationForm(request.POST, request.FILES)  # form 가져오자    주의! files는 request.FILES로 꼭 지정해줘야 함
        if form.is_valid():
            form.save()  # new_product 저장하자
        return redirect('product:list2')
    else:  # 빈 폼
        form = ProductCreationForm()
    return render(request, 'product/product_create.html', {'form': form})


def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)  # pk에 해당하는 product 가져오자
    if request.method == 'POST':  # 사용자가 입력하고 버튼 눌렀을 때
        form = ProductChangeForm(request.POST, request.FILES,
                                 instance=product)  # form 가져오자    주의! files는 request.FILES로 꼭 지정해줘야 함
        if form.is_valid():
            form.save()  # 수정한 product 저장하자
        return redirect('product:list2')
    else:
        form = ProductChangeForm(instance=product)
    return render(request, 'product/product_update.html', {'form': form, 'product': product})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)  # pk에 해당하는 product 가져오자
    if request.method == 'POST':  # 사용자가 입력하고 버튼 눌렀을 때
        product.delete()  # product 삭제하자
        return redirect('product:list2')
    else:
        pass
    return render(request, 'product/product_confirm_delete.html', {'product': product})


def add2_review(request, product_pk):
    if request.method == 'POST':
        form = ReviewCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('product:detail2', pk=product_pk)
    else:
        product = get_object_or_404(Product, pk=product_pk)
        initial = {'product': product}
        form = ReviewCreationForm(initial=initial)
        context = {'form': form, 'product': product}
    return render(request, 'product/review_create.html', context)


def edit2_review(request, product_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'POST':
        form = ReviewChangeForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
        return redirect('product:detail2', pk=product_pk)
    else:
        form = ReviewChangeForm(instance=review)
        context = {'form': form}
    return render(request, 'product/review_update.html', context)
