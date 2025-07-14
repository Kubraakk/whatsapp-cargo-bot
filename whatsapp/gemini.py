from vertexai.language_models import ChatModel

def ask_gemini(prompt):
    model = ChatModel.from_pretrained("chat-bison")
    chat = model.start_chat()
    response = chat.send_message(prompt)
    return response.text
