import os
from dotenv import load_dotenv
import sys

# Ensure that you have the exception.py file in the same directory
from exception import customexception  
from llama_index.llms.gemini import Gemini
from exception import customexception
import google.generativeai as genai
import logging


# Load environment variables from .env file if needed
load_dotenv()

# Set your Google API Key here or use .env
os.environ['GOOGLE_API_KEY'] = "AIzaSyCvayD7XmfAm1T0QlDTyu6euPBCGHJr9qo"
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY is None:
    raise customexception("Google API Key not found. Please ensure it is set in the .env file or environment.", sys)

genai.configure(api_key=GOOGLE_API_KEY)

def load_model():
    """
    Loads a Gemini-Pro model for natural language processing.

    Returns:
    - Gemini: An instance of the Gemini class initialized with the 'gemini-pro' model.
    """
    try:
        model = Gemini(models='gemini-pro', api_key=GOOGLE_API_KEY)
        return model
    except Exception as e:
        raise customexception(e, sys)

# Example usage
if __name__ == "__main__":
    try:
        model = load_model()
        print("Model loaded successfully.")
    except customexception as ce:
        logging.error(f"An error occurred: {ce}")
        sys.exit(1)
