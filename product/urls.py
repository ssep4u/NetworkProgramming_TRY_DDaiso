from django.urls import path

from product import views
from product.views import ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView

app_name = 'product'

urlpatterns = [
    path('list/', ProductListView.as_view(), name='list'),  # product:list
    path('list2/', views.list_product, name='list2'),  # product:list2
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),  # product:detail
    path('detail2/<int:pk>/', views.detail_product, name='detail2'),  # product:detail2
    path('add/', ProductCreateView.as_view(), name='add'),  # product:add
    path('add2/', views.create_product, name='add2'),  # product:add2
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),  # product:edit
    path('edit2/<int:pk>/', views.update_product, name='edit2'),  # product:edit2
    path('remove/<int:pk>/', ProductDeleteView.as_view(), name='remove'),  # product:remove
    path('remove2/<int:pk>/', views.delete_product, name='remove2'),  # product:remove
    path('product/<int:product_pk>/add2_review/', views.add2_review, name='add2_review'),  # product:add2_review
    path('product/<int:product_pk>/edit2_review/<int:review_pk>/', views.edit2_review, name='edit2_review'),  # product:edit2_review
    path('product/<int:product_pk>/remove2_review/<int:review_pk>/', views.remove2_review, name='remove2_review'),  # product:remove2_review
]
