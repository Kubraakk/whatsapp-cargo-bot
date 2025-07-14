import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_whatsapp_reply(to, body):
    url = f"https://api.twilio.com/2010-04-01/Accounts/{os.getenv('TWILIO_ACCOUNT_SID')}/Messages.json"
    payload = {
        "From": os.getenv("TWILIO_WHATSAPP_NUMBER"),
        "To": to,
        "Body": body,
    }
    auth = (os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

    response = requests.post(url, data=payload, auth=auth)
    print("📤 Yanıt gönderildi:", response.status_code, response.text)
