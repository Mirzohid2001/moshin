from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ContactMessage
from .services import TelegramService
from products.models import Order

@receiver(post_save, sender=ContactMessage)
def send_contact_to_telegram(sender, instance, created, **kwargs):
    """Отправка контактного сообщения в Telegram при создании"""
    if created:
        message = TelegramService.format_contact_message(instance)
        TelegramService.send_message(message)

@receiver(post_save, sender=Order)
def send_order_to_telegram(sender, instance, created, **kwargs):
    """Отправка заказа в Telegram при создании"""
    if created:
        message = TelegramService.format_order_message(instance)
        TelegramService.send_message(message) 