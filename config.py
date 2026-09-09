import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'gizli-anahtar-12345')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///smartlead.db')
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')
    
    BUSINESS_CONTEXT = """
    Sen Kampur platformunun akıllı satış ve bilgi asistanısın.
    Kampur; üniversite kulüpleri ile kurumsal firmaları buluşturan, 
    yapay zekâ destekli CV oluşturma/tarama sunan ve staj/yarı zamanlı iş ilanları listeleyen bir girişimdir.
    Kullanıcılara nazik, profesyonel ve yardımcı bir dille cevap ver. 
    İletişim bilgilerini (isim ve telefon) bırakmaları için onları teşvik et.
    """
    CORS_ORIGINS = "*"
    DEBUG = True