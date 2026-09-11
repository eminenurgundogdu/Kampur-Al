import os
from groq import Groq
from dotenv import load_dotenv
from config import Config

# .env dosyasındaki ortam değişkenlerini ortama yükler
load_dotenv()

# Groq istemcisini başlatıyoruz (API anahtarını Config sınıfı üzerinden .env'den alır)
client = Groq(api_key=Config.GROQ_API_KEY)

def get_ai_response(user_message):
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": Config.BUSINESS_CONTEXT},
                {"role": "user", "content": user_message},
            ],
            temperature=0.7,
            max_tokens=1024,
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"HATA DETAYI: {e}")
        return f"Groq Hatası: {str(e)}"