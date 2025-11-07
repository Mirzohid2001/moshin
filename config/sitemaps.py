from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import BlogPost
from products.models import Product


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return [
            "blog:home",
            "blog:about",
            "blog:blog_list",
            "products:product_list",
            "products:category_list",
            "partners:partner_list",
            "contact:contact",
        ]

    def location(self, item):
        return reverse(item)


class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return BlogPost.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.updated_at


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Product.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at

