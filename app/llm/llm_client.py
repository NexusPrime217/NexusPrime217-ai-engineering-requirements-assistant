from google import genai
from app.core.config import setting
from app.rag.prompt_builder import build_prompt

client = genai.Client(
    api_key=setting.GEMINI_API_KEY
)

def generate_answer(prompt: str):
    response = client.models.generate_content(
        model = setting.LLM_MODEL,
        contents = prompt,
    )

    return response.text

contexts = [
    "JWT access tokens expire after 30 minutes."
]

prompt = build_prompt(
    "When does the JWT token expire?",
    contexts
)

print(generate_answer(prompt))