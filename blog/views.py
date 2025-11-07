from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from products.models import Product

from .models import CompanyInfo, CompanyCapability, BlogPost

def home(request):
    """Главная страница"""
    company_info = CompanyInfo.objects.first()
    capabilities = CompanyCapability.objects.filter(is_active=True)
    recent_posts = BlogPost.objects.filter(published=True)[:3]
    featured_products = (
        Product.objects.filter(is_active=True)
        .select_related('category')
        .order_by('-created_at')[:4]
    )
    
    context = {
        'company_info': company_info,
        'capabilities': capabilities,
        'recent_posts': recent_posts,
        'featured_products': featured_products,
    }
    return render(request, 'blog/home.html', context)

def about(request):
    """Страница о компании"""
    company_info = CompanyInfo.objects.first()
    capabilities = CompanyCapability.objects.filter(is_active=True)
    
    context = {
        'company_info': company_info,
        'capabilities': capabilities,
    }
    return render(request, 'blog/about.html', context)

class BlogListView(ListView):
    """Список записей блога"""
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        return BlogPost.objects.filter(published=True)

class BlogDetailView(DetailView):
    """Детальная страница записи блога"""
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        return BlogPost.objects.filter(published=True)
