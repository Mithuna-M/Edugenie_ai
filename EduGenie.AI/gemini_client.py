import os
from typing import Optional

from dotenv import load_dotenv
from google import genai


load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3-flash-preview"
)


_client: Optional[genai.Client] = None


def get_client() -> genai.Client:
    """
    Create the Gemini client lazily.
    """

    global _client

    if _client is not None:
        return _client

    if not GEMINI_API_KEY:
        raise RuntimeError(
            "GEMINI_API_KEY is not configured. "
            "Please add your Gemini API key to the .env file."
        )

    if GEMINI_API_KEY == "YOUR_GEMINI_API_KEY_HERE":
        raise RuntimeError(
            "Please replace YOUR_GEMINI_API_KEY_HERE "
            "with your real Gemini API key in the .env file."
        )

    _client = genai.Client(
        api_key=GEMINI_API_KEY
    )

    return _client


def generate_text(
    prompt: str,
    system_instruction: Optional[str] = None,
) -> str:
    """
    Send a prompt to Gemini and return generated text.
    """

    client = get_client()

    config = None

    if system_instruction:
        config = {
            "system_instruction": system_instruction
        }

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=config,
    )

    text = getattr(
        response,
        "text",
        None
    )

    if not text:
        raise RuntimeError(
            "Gemini returned an empty response."
        )

    return text.strip()