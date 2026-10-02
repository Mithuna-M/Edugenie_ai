import os

from dotenv import load_dotenv


load_dotenv()


USE_LOCAL_EXPLAINER = (
    os.getenv(
        "USE_LOCAL_EXPLAINER",
        "true"
    ).lower()
    in {"true", "1", "yes"}
)


LOCAL_MODEL_NAME = os.getenv(
    "LOCAL_EXPLAINER_MODEL",
    "MBZUAI/LaMini-Flan-T5-783M"
)


_pipeline = None


def _load_local_pipeline():
    """
    Load the local Hugging Face model only when needed.
    """

    global _pipeline

    if _pipeline is not None:
        return _pipeline

    from transformers import pipeline

    _pipeline = pipeline(
        "text2text-generation",
        model=LOCAL_MODEL_NAME,
    )

    return _pipeline


def _local_explanation(topic: str) -> str:
    """
    Generate a beginner-friendly explanation
    using the local LaMini-Flan-T5 model.
    """

    generator = _load_local_pipeline()

    prompt = f"""
Explain the following topic to a beginner.

Topic:
{topic}

Requirements:
- Use simple language.
- Define important terms.
- Explain the main idea clearly.
- Give one simple example.
- Keep the explanation concise.
"""

    result = generator(
        prompt,
        max_new_tokens=300,
        do_sample=False,
    )

    if not result:
        raise RuntimeError(
            "Local model returned an empty response."
        )

    return result[0]["generated_text"].strip()


def _gemini_explanation(topic: str) -> str:
    """
    Generate an explanation using Gemini.
    """

    from gemini_client import generate_text

    prompt = f"""
Explain the following concept to a beginner.

Topic:
{topic}

Requirements:
1. Give a simple definition.
2. Explain how it works.
3. Give an easy example.
4. Mention why it is useful.
5. Keep the explanation clear and concise.
"""

    return generate_text(
        prompt,
        system_instruction=(
            "You explain academic concepts to beginners "
            "using simple and clear language."
        ),
    )


def explain_topic(topic: str) -> str:
    """
    Main explanation function.
    """

    if not topic or not topic.strip():
        raise ValueError(
            "Topic cannot be empty."
        )

    topic = topic.strip()

    if USE_LOCAL_EXPLAINER:

        try:
            return _local_explanation(topic)

        except Exception:
            # If the local model fails,
            # use Gemini as a fallback.
            return _gemini_explanation(topic)

    return _gemini_explanation(topic)