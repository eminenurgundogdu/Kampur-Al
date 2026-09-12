from flask import Blueprint, request, jsonify
from flask_cors import CORS
from services.ai_service import get_ai_response

main_bp = Blueprint('main', __name__)
CORS(main_bp)  # Wix Studio'dan gelecek isteklerin engellenmesini önler

@main_bp.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Kampur AI Backend Çalışıyor!"})

# --- KULLANICI CHAT ENDPOINT'İ ---
@main_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')
    if not message:
        return jsonify({"error": "Mesaj boş olamaz"}), 400
    
    response = get_ai_response(message)
    return jsonify({"response": response})
    
@main_bp.route('/leads', methods=['POST'])
def yeni_lead():
    veri = request.get_json() or {}
    isim = veri.get('isim')
    telefon = veri.get('telefon')
    mesaj = veri.get('mesaj', '')
    
    if not isim or not telefon:
        return jsonify({"basari": False, "hata": "İsim ve telefon zorunludur"}), 400
    
    # lead_ekle(isim, telefon, mesaj)  # Veritabanı veya servis kaydı
    return jsonify({"basari": True, "mesaj": "Talebiniz başarıyla alındı"}), 201
    
# --- YÖNETİM PANELİ (DASHBOARD) ENDPOINT'LERİ ---
@main_bp.route('/dashboard/stats', methods=['GET'])
def get_dashboard_stats():
    # Yönetim panelindeki göstergeler için örnek istatistik verisi
    stats_data = {
        "total_chats": 124,
        "active_users": 38,
        "popular_topics": ["CV Hazırlama", "Staj İlanları", "Etkinlikler"]
    }
    return jsonify(stats_data)

@main_bp.route('/dashboard/logs', methods=['GET'])
def get_chat_logs():
    # Yönetim panelindeki tablo için son sohbet logları
    logs = [
        {"user": "Öğrenci 1", "prompt": "CV nasıl hazırlanır?", "date": "2026-09-09"},
        {"user": "Öğrenci 2", "prompt": "Etkinlikler ne zaman?", "date": "2026-09-09"}
    ]
    return jsonify({"logs": logs})
