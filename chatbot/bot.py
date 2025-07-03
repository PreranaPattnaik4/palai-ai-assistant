import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("AIzaSyDhMIkeWDEFATOMvftsVkd-luCiyTO2wNI")

# Configure Gemini with latest API
genai.configure(api_key=api_key)

# Load the correct model (this should work for most users)
try:
    model = genai.GenerativeModel(model_name="models/gemini-pro")
except Exception as e:
    model = None
    print("Model loading error:", str(e))

# Get response function
def get_bot_response(user_input):
    if not model:
        return "Model couldn't be loaded. Check your API key or model name."

    try:
        response = model.generate_content(user_input)

        # Check if response has text
        if hasattr(response, 'text'):
            return response.text.strip()
        else:
            return "Gemini didn't return a valid response."

    except Exception as e:
        return f"Error talking to Gemini: {str(e)}"
