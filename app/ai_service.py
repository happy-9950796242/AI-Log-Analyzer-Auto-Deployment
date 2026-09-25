from openai import OpenAI
from app.config import settings


client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_ai_analysis(log_message: str, level: str):

    prompt = f"""
You are an expert DevOps log analyzer.

Analyze this application log:

Log level: {level}
Log message: {log_message}

Provide:
1. Severity
2. Problem
3. Possible Cause
4. Suggested Solution

Keep the answer concise and practical.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return {
        "analysis": response.output_text
    }