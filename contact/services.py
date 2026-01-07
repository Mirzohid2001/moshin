import requests
from django.conf import settings
from django.utils import timezone

class TelegramService:
    @staticmethod
    def send_message(message):
        """Отправка сообщения в Telegram"""
        if not settings.TELEGRAM_BOT_TOKEN or not settings.TELEGRAM_CHAT_ID:
            return False
        
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {
            'chat_id': settings.TELEGRAM_CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'
        }
        
        try:
            response = requests.post(url, data=data)
            return response.status_code == 200
        except Exception as e:
            print(f"Ошибка отправки в Telegram: {e}")
            return False
    
    @staticmethod
    def format_contact_message(contact):
        """Форматирование контактного сообщения для Telegram"""
        message = f"""
🔔 <b>Новое контактное сообщение</b>

👤 <b>Имя:</b> {contact.name}
📧 <b>Email:</b> {contact.email}
📞 <b>Телефон:</b> {contact.phone}
📝 <b>Тема:</b> {contact.subject}

💬 <b>Сообщение:</b>
{contact.message}

⏰ <b>Дата:</b> {contact.created_at.strftime('%d.%m.%Y %H:%M')}
        """
        return message.strip()
    
    @staticmethod
    def format_order_message(order):
        """Форматирование заказа для Telegram"""
        # Коэффициент перевода тонн в литры (для нефтепродуктов)
        # Для дизельного топлива: ~1150 л/тонна, для бензина: ~1350 л/тонна
        # Используем средний коэффициент 1200 л/тонна
        LITERS_PER_TON = 1200
        
        quantity_tons = order.quantity
        price_per_liter = order.product.price
        total_liters = quantity_tons * LITERS_PER_TON
        total_cost = price_per_liter * total_liters
        
        message = f"""
🛒 <b>Новый заказ продукта</b>

👤 <b>Клиент:</b> {order.customer_name}
📧 <b>Email:</b> {order.customer_email}
📞 <b>Телефон:</b> {order.customer_phone}

📦 <b>Продукт:</b> {order.product.name}
🔢 <b>Количество:</b> {quantity_tons} тонн ({total_liters:,.0f} литров)
💰 <b>Цена за литр:</b> {price_per_liter:,.2f} сум
💵 <b>Общая стоимость:</b> {total_cost:,.2f} сум

💬 <b>Дополнительное сообщение:</b>
{order.message if order.message else 'Не указано'}

⏰ <b>Дата заказа:</b> {order.created_at.strftime('%d.%m.%Y %H:%M')}
        """
        return message.strip() 