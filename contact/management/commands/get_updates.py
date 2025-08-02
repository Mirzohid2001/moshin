from django.core.management.base import BaseCommand
from django.conf import settings
import requests
import json

class Command(BaseCommand):
    help = 'Получение обновлений Telegram бота для определения Chat ID'

    def handle(self, *args, **options):
        self.stdout.write("Получение обновлений Telegram бота...")
        
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/getUpdates"
        
        try:
            response = requests.get(url, timeout=10)
            self.stdout.write(f"Статус ответа: {response.status_code}")
            
            if response.status_code == 200:
                updates = response.json()
                if updates.get('ok'):
                    results = updates.get('result', [])
                    
                    if results:
                        self.stdout.write(
                            self.style.SUCCESS(f"✅ Найдено {len(results)} обновлений!")
                        )
                        
                        for i, update in enumerate(results):
                            self.stdout.write(f"\n--- Обновление {i+1} ---")
                            
                            if 'message' in update:
                                message = update['message']
                                chat = message.get('chat', {})
                                self.stdout.write(f"Chat ID: {chat.get('id')}")
                                self.stdout.write(f"Chat Type: {chat.get('type')}")
                                self.stdout.write(f"Chat Title: {chat.get('title', 'N/A')}")
                                self.stdout.write(f"Chat Username: {chat.get('username', 'N/A')}")
                                
                                if message.get('text'):
                                    self.stdout.write(f"Message: {message['text'][:50]}...")
                            
                            elif 'channel_post' in update:
                                channel_post = update['channel_post']
                                chat = channel_post.get('chat', {})
                                self.stdout.write(f"Channel ID: {chat.get('id')}")
                                self.stdout.write(f"Channel Title: {chat.get('title', 'N/A')}")
                                self.stdout.write(f"Channel Username: {chat.get('username', 'N/A')}")
                    else:
                        self.stdout.write(
                            self.style.WARNING("⚠️ Обновлений не найдено. Отправьте сообщение боту или добавьте его в группу.")
                        )
                else:
                    self.stdout.write(
                        self.style.ERROR(f"❌ Ошибка получения обновлений: {updates}")
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
        self.stdout.write("ИНСТРУКЦИИ:")
        self.stdout.write("1. Добавьте бота в группу/канал")
        self.stdout.write("2. Отправьте сообщение в группу/канал")
        self.stdout.write("3. Запустите команду снова для получения Chat ID")
        self.stdout.write("4. Обновите TELEGRAM_CHAT_ID в settings.py")
        self.stdout.write("="*50) 