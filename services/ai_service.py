import os
from groq import Groq
from config import Config

# Groq client başlatılıyor
client = Groq(api_key=Config.GROQ_API_KEY)

def get_ai_response(user_message):
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": Config.BUSINESS_CONTEXT},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=1024,
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Groq API Hatası: {e}")
        return "Üzgünüm, şu anda yanıt üretemiyorum. Lütfen daha sonra tekrar deneyiniz."