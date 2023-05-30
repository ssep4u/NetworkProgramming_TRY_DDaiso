from django.urls import path

from product import views
from product.views import ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView

app_name = 'product'

urlpatterns = [
    path('list/', ProductListView.as_view(), name='list'),  # product:list
    path('list2/', views.list_product, name='list2'),  # product:list2
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),  # product:detail
    path('add/', ProductCreateView.as_view(), name='add'),  # product:add
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),  # product:edit
    path('remove/<int:pk>/', ProductDeleteView.as_view(), name='remove'),  # product:remove
]
