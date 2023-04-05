from django.urls import path

from product.views import ProductListView

app_name = 'product'

urlpatterns = [
    path('list/', ProductListView.as_view(), name='list'),  #product:list
]
