import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables from .env file
load_dotenv()

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    
    # 🌟 CHANGED THIS LINE: Updated to a supported, state-of-the-art model
    MODEL_NAME = "llama-3.3-70b-versatile" 

def get_llm():
    if not Config.GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is missing! Check your .env file.")
    
    return ChatGroq(
        groq_api_key=Config.GROQ_API_KEY,
        model_name=Config.MODEL_NAME,
        temperature=0.1
    )