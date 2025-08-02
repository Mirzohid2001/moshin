from django.core.management.base import BaseCommand
from django.conf import settings
import requests

class Command(BaseCommand):
    help = 'Получение информации о Telegram боте'

    def handle(self, *args, **options):
        self.stdout.write("Получение информации о Telegram боте...")
        
        # Получаем информацию о боте
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/getMe"
        
        try:
            response = requests.get(url, timeout=10)
            self.stdout.write(f"Статус ответа: {response.status_code}")
            
            if response.status_code == 200:
                bot_info = response.json()
                if bot_info.get('ok'):
                    bot_data = bot_info['result']
                    self.stdout.write(
                        self.style.SUCCESS(f"✅ Бот найден!")
                    )
                    self.stdout.write(f"Имя бота: {bot_data.get('first_name', 'N/A')}")
                    self.stdout.write(f"Username: @{bot_data.get('username', 'N/A')}")
                    self.stdout.write(f"ID бота: {bot_data.get('id', 'N/A')}")
                    self.stdout.write(f"Может присоединяться к группам: {bot_data.get('can_join_groups', 'N/A')}")
                    self.stdout.write(f"Может читать сообщения: {bot_data.get('can_read_all_group_messages', 'N/A')}")
                else:
                    self.stdout.write(
                        self.style.ERROR(f"❌ Ошибка получения информации о боте: {bot_info}")
                    )
            else:
                self.stdout.write(
                    self.style.ERROR(f"❌ Ошибка HTTP: {response.status_code}")
                )
                self.stdout.write(f"Ответ: {response.text}")
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Исключение: {e}')
            )
        
        self.stdout.write("\n" + "="*50)
        self.stdout.write("ИНСТРУКЦИИ ПО НАСТРОЙКЕ:")
        self.stdout.write("1. Добавьте бота в группу/канал как администратора")
        self.stdout.write("2. Отправьте сообщение в группу/канал")
        self.stdout.write("3. Получите правильный Chat ID через @userinfobot")
        self.stdout.write("4. Обновите TELEGRAM_CHAT_ID в settings.py")
        self.stdout.write("="*50) 