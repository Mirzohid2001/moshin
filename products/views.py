from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from .models import Category, Product, Order
from .forms import OrderForm

class CategoryListView(ListView):
    """Список категорий"""
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'categories'

class ProductListView(ListView):
    """Список продуктов"""
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            context['current_category'] = get_object_or_404(Category, slug=category_slug)
        return context

class ProductDetailView(DetailView):
    """Детальная страница продукта"""
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    
    def get_queryset(self):
        return Product.objects.filter(is_active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_form'] = OrderForm()
        context['related_products'] = Product.objects.filter(
            category=self.object.category,
            is_active=True
        ).exclude(id=self.object.id)[:4]
        return context

def create_order(request, product_id):
    """Создание заказа"""
    product = get_object_or_404(Product, id=product_id, is_active=True)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            messages.success(request, 'Ваш заказ успешно отправлен! Мы свяжемся с вами в ближайшее время.')
            return redirect('products:product_detail', slug=product.slug)
    else:
        form = OrderForm()
    
    context = {
        'product': product,
        'order_form': form,
    }
    return render(request, 'products/product_detail.html', context)
