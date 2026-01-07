from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='categories/', verbose_name="Изображение", blank=True, null=True)
    order = models.IntegerField(default=0, verbose_name="Порядок")
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['order']
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:product_list_by_category", args=[self.slug])

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="URL")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    description = models.TextField(verbose_name="Описание")
    specifications = models.TextField(blank=True, verbose_name="Технические характеристики")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение", blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['name']
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:product_detail", args=[self.slug])

class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('processing', 'В обработке'),
        ('completed', 'Завершен'),
        ('cancelled', 'Отменен'),
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    customer_name = models.CharField(max_length=200, verbose_name="Имя клиента")
    customer_email = models.EmailField(verbose_name="Email клиента")
    customer_phone = models.CharField(max_length=20, verbose_name="Телефон клиента")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество (тонн)")
    message = models.TextField(blank=True, verbose_name="Дополнительное сообщение")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Заказ {self.id} - {self.customer_name}"
