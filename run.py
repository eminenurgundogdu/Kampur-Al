import sys
import os

# Ana proje dizinini Python yoluna ekle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from flask_cors import CORS
from config import Config
from APP.routes import main_bp

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
app.register_blueprint(main_bp)

if __name__ == '__main__':
    print("Kampur AI Backend başlatılıyor...")
    app.run(host='127.0.0.1', port=5000, debug=True)