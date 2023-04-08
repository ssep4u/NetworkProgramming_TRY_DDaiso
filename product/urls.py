from django.urls import path

from product.views import ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView

app_name = 'product'

urlpatterns = [
    path('list/', ProductListView.as_view(), name='list'),  # product:list
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),  # product:detail
    path('add/', ProductCreateView.as_view(), name='add'),  # product:add
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),  # product:edit
]
