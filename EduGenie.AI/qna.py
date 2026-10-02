from gemini_client import generate_text


def answer_question(question: str) -> str:
    """
    Answer an educational question using Gemini.
    """

    if not question or not question.strip():
        raise ValueError("Question cannot be empty.")

    prompt = f"""
You are EduGenie, an educational AI assistant.

Answer the student's question clearly and accurately.

Question:
{question}

Instructions:
- Give a direct answer.
- Explain difficult terms simply.
- Use examples when useful.
- Avoid unnecessary complexity.
- Do not invent facts.
- Use short paragraphs or bullet points.
"""

    return generate_text(
        prompt,
        system_instruction=(
            "You are a helpful educational assistant. "
            "Your explanations should be accurate, "
            "concise, beginner-friendly, and easy to understand."
        ),
    )