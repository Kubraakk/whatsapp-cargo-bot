from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .utils import send_whatsapp_reply
from .gemini import ask_gemini
import json
import asyncio

@csrf_exempt
def whatsapp_webhook(request):
    if request.method == 'POST':
        message = request.POST.get("Body")
        sender = request.POST.get("From")

        print(f"📥 Yeni mesaj: '{message}' - Gönderen: {sender}")
        handle_whatsapp_message(sender, message)

        return JsonResponse({"status": "ok"}, status=200)
    return JsonResponse({"error": "Invalid method"}, status=400)


def handle_whatsapp_message(sender_id, text):
    if text.lower().strip() == "merhaba":
        send_whatsapp_reply(sender_id, "👋 Merhaba! Sipariş numaranızı yazarsanız kargonuzu kontrol edebilirim.")
    else:
        response = asyncio.run(ask_gemini(text))
        send_whatsapp_reply(sender_id, response)
