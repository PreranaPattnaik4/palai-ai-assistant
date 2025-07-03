import google.generativeai as genai
from dotenv import load_dotenv
import os

# ✅ Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# ✅ Configure the Gemini API
genai.configure(api_key=api_key)

# ✅ List and display available models
models = genai.list_models()
for model in models:
    print(f"{model.name} - {model.supported_generation_methods}")
