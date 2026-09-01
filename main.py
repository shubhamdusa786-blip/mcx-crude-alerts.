import os
import requests
from datetime import datetime

TELEGRAM_BOT_TOKEN = os.environ["8886695615:AAETXKEQqaFhYGxwfc3ZgKw44r4WXbp-YY4"]
TELEGRAM_CHAT_ID = os.environ["663283155"]

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    response = requests.post(
        url,
        json={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        },
        timeout=20
    )
    response.raise_for_status()

send_telegram_alert(
    "✅ MCX Crude alert system test successful
"
    + datetime.now().strftime("%d-%m-%Y %H:%M:%S")
)
