import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyDhMIkeWDEFATOMvftsVkd-luCiyTO2wNI"))

# Initialize Gemini Pro model
model = genai.GenerativeModel("gemini-pro")

# Function to get response from Gemini
def get_gemini_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
