from django.db import models
from django.utils import timezone

class ContactMessage(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    subject = models.CharField(max_length=200, verbose_name="Тема")
    message = models.TextField(verbose_name="Сообщение")
    is_read = models.BooleanField(default=False, verbose_name="Прочитано")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    class Meta:
        verbose_name = "Контактное сообщение"
        verbose_name_plural = "Контактные сообщения"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

class ContactInfo(models.Model):
    address = models.TextField(verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    working_hours = models.CharField(max_length=200, verbose_name="Рабочие часы")
    map_embed = models.TextField(blank=True, verbose_name="Код карты")
    
    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактная информация"
    
    def __str__(self):
        return "Контактная информация"
