from django.urls import path

from product.views import ProductListView, ProductDetailView

app_name = 'product'

urlpatterns = [
    path('list/', ProductListView.as_view(), name='list'),  # product:list
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),  # product:detail
]
