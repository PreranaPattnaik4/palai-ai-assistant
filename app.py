from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ✅ Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# ✅ Configure the API with the key
genai.configure(api_key=api_key)

# ✅ Use correct model name from your list
model = genai.GenerativeModel('gemini-1.5-pro')

# ✅ Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    try:
        response = model.generate_content(user_message)
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"Error: {str(e)}"

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
