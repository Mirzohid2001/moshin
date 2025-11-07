from django.db import models
from django.urls import reverse

class CompanyInfo(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    image = models.ImageField(upload_to='company/', verbose_name="Изображение", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    
    class Meta:
        verbose_name = "Информация о компании"
        verbose_name_plural = "Информация о компании"
    
    def __str__(self):
        return self.title

class CompanyCapability(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    icon = models.CharField(max_length=100, verbose_name="Иконка", help_text="CSS класс иконки")
    order = models.IntegerField(default=0, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    class Meta:
        verbose_name = "Возможность компании"
        verbose_name_plural = "Возможности компании"
        ordering = ['order']
    
    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(unique=True, verbose_name="URL")
    content = models.TextField(verbose_name="Содержание")
    excerpt = models.TextField(max_length=500, verbose_name="Краткое описание")
    image = models.ImageField(upload_to='blog/', verbose_name="Изображение", blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Опубликовано")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    
    class Meta:
        verbose_name = "Запись блога"
        verbose_name_plural = "Записи блога"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:blog_detail", args=[self.slug])
