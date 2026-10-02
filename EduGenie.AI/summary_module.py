from gemini_client import generate_text


def summarize_text(text: str) -> str:
    """
    Summarize educational content
    into concise study material.
    """

    if not text or not text.strip():
        raise ValueError(
            "Text cannot be empty."
        )

    prompt = f"""
Summarize the following educational passage.

PASSAGE:
{text}

Requirements:
- Preserve the important information.
- Remove repetition.
- Use simple language.
- Keep important terminology.
- Organize the result using short paragraphs
  or bullet points.
- Do not add information that is not present
  in the passage.
"""

    return generate_text(
        prompt,
        system_instruction=(
            "You are an educational summarization "
            "assistant. Create accurate and concise "
            "study-friendly summaries."
        ),
    )