from app.rag.prompt_builder import build_prompt
from app.services.search_service import semantic_search
from app.llm.llm_client import generate_answer

def answer_question(
        question:str,
        user_id:int
):
    contexts = semantic_search(
        question,
        user_id
    )

    if not contexts:
        return "I couldn't find any relevant information in the uploaded documents."

    prompt = build_prompt(
        question,
        contexts
    )

    return generate_answer(prompt)