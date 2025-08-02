from django.core.management.base import BaseCommand
from django.conf import settings
import requests

class Command(BaseCommand):
    help = 'Тестирование отправки сообщений в Telegram'

    def handle(self, *args, **options):
        self.stdout.write("Проверка настроек Telegram...")
        self.stdout.write(f"Bot Token: {settings.TELEGRAM_BOT_TOKEN[:20]}...")
        self.stdout.write(f"Chat ID: {settings.TELEGRAM_CHAT_ID}")
        
        test_message = """
🔔 <b>Тестовое сообщение от Isomer Oil</b>

✅ <b>Статус:</b> Telegram бот успешно настроен!
📅 <b>Дата:</b> Тестовое сообщение
💬 <b>Сообщение:</b> Система уведомлений работает корректно.

🎉 <b>Готово к работе!</b>
        """
        
        self.stdout.write("Отправка тестового сообщения в Telegram...")
        
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {
            'chat_id': settings.TELEGRAM_CHAT_ID,
            'text': test_message.strip(),
            'parse_mode': 'HTML'
        }
        
        try:
            response = requests.post(url, data=data, timeout=10)
            self.stdout.write(f"Статус ответа: {response.status_code}")
            self.stdout.write(f"Ответ: {response.text}")
            
            if response.status_code == 200:
                self.stdout.write(
                    self.style.SUCCESS('✅ Тестовое сообщение успешно отправлено в Telegram!')
                )
            else:
                self.stdout.write(
                    self.style.ERROR(f'❌ Ошибка отправки сообщения в Telegram! Статус: {response.status_code}')
                )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Исключение при отправке: {e}')
            ) 