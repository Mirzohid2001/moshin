from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<slug:category_slug>/', views.ProductListView.as_view(), name='product_list_by_category'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('<int:product_id>/order/', views.create_order, name='create_order'),
] 