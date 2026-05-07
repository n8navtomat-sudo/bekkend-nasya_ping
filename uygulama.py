from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client
import os

app = Flask(__name__)
CORS(app)

supabase = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_KEY"])

@app.route('/api/bot-qabul', methods=['POST'])
def register():
    data = request.json
    supabase.table("Ro'yhatdan otish").insert({"chat_id": data['telegramUserId'], "isim": data['storeName'], "tel_raqam": data['phoneNumber']}).execute()
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
