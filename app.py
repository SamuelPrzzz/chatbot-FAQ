from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Base de datos improvisada
faq_responses = {
    "horario": (
        "Nuestros horarios de atencion son de lunes a domingo de 11:00 a.m. a 10:00 p.m."
    ),
    
    "ubicacion": (
        "Estamos ubicados en varias locaciones de Maracaibo, incluyendo en el C.C. Sambil!!"
    ),
    
    "ubicación": (
        "Estamos ubicados en varias locaciones de Maracaibo, incluyendo en el C.C. Sambil!!"
    ),
    
    "menu": (
        "Puedes consultar nuestros productos y ofertas del dia directamente en mostrador o en nuestra app."
    ),
    
    "menú": (
        "Puedes consultar nuestros productos y ofertas del dia directamente en mostrador o en nuestra app."
    ),
}


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/webhook", methods=["POST"])
def chatbot_webhook():
    data = request.get_json()
    user_message = data.get("message", "").lower()
    user_id = data.get("user_id", "guest")
    
    # Respuesta por defecto si el bot no entiende
    response_text = (
        "Lo siento, soy un bot en desarrollo. Escribe 'Horario', 'Ubicación' o 'Menú'"
    )

    for keyword, answer in faq_responses.items():
        if keyword in user_message:
            response_text = answer
            break 
        
    response_payload = {
        "status": "success",
        "user_id": user_id,
        "reply": response_text,
    }
    
    return jsonify(response_payload), 200

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 5000)