from django.db import models
from django.utils import timezone

class Partner(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название компании")
    description = models.TextField(verbose_name="Описание")
    logo = models.ImageField(upload_to='partners/', verbose_name="Логотип")
    website = models.URLField(blank=True, verbose_name="Веб-сайт")
    email = models.EmailField(blank=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    address = models.TextField(blank=True, verbose_name="Адрес")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    order = models.IntegerField(default=0, verbose_name="Порядок")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"
        ordering = ['order']
    
    def __str__(self):
        return self.name

class Partnership(models.Model):
    PARTNERSHIP_TYPE_CHOICES = [
        ('supplier', 'Поставщик'),
        ('client', 'Клиент'),
        ('distributor', 'Дистрибьютор'),
        ('service', 'Сервисный партнер'),
        ('other', 'Другое'),
    ]
    
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name="Партнер")
    partnership_type = models.CharField(max_length=20, choices=PARTNERSHIP_TYPE_CHOICES, verbose_name="Тип партнерства")
    description = models.TextField(verbose_name="Описание сотрудничества")
    start_date = models.DateField(verbose_name="Дата начала сотрудничества")
    end_date = models.DateField(blank=True, null=True, verbose_name="Дата окончания сотрудничества")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    class Meta:
        verbose_name = "Партнерство"
        verbose_name_plural = "Партнерства"
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.partner.name} - {self.get_partnership_type_display()}"
