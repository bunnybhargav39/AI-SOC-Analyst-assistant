import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_log_ai(log):

    prompt = f"""
You are a SOC analyst.

Analyze this security log:

{log}

Provide:
1. Severity
2. Threat Type
3. Explanation
4. Recommendation

Keep response short and professional.
"""

    response = model.generate_content(prompt)

    return response.text
