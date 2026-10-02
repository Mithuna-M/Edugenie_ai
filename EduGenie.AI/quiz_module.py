import json
import re
from typing import Any

from gemini_client import generate_text


def clean_json_block(text: str) -> str:
    """
    Remove Markdown code fences from an AI response.
    """

    text = text.strip()

    text = re.sub(
        r"^```(?:json)?\s*",
        "",
        text,
        flags=re.IGNORECASE,
    )

    text = re.sub(
        r"\s*```$",
        "",
        text,
    )

    return text.strip()


def _validate_quiz(data: Any) -> list[dict]:
    """
    Validate the generated quiz.

    EduGenie requires:
    - exactly 3 questions
    - exactly 4 options per question
    - one correct answer
    """

    if not isinstance(data, list):
        raise ValueError(
            "Quiz response must be a JSON list."
        )

    if len(data) != 3:
        raise ValueError(
            "Quiz must contain exactly 3 questions."
        )

    validated = []

    for index, question in enumerate(
        data,
        start=1
    ):

        if not isinstance(question, dict):
            raise ValueError(
                f"Question {index} must be an object."
            )

        question_text = question.get(
            "question"
        )

        options = question.get(
            "options"
        )

        answer = question.get(
            "answer"
        )

        if not isinstance(
            question_text,
            str
        ):
            raise ValueError(
                f"Question {index} has an invalid question."
            )

        if not isinstance(
            options,
            list
        ):
            raise ValueError(
                f"Question {index} options must be a list."
            )

        if len(options) != 4:
            raise ValueError(
                f"Question {index} must have exactly 4 options."
            )

        if not all(
            isinstance(option, str)
            for option in options
        ):
            raise ValueError(
                f"Question {index} contains invalid options."
            )

        if not isinstance(
            answer,
            str
        ):
            raise ValueError(
                f"Question {index} has an invalid answer."
            )

        cleaned_options = [
            option.strip()
            for option in options
        ]

        cleaned_answer = answer.strip()

        if cleaned_answer not in cleaned_options:
            raise ValueError(
                f"Question {index} answer must match one of the options."
            )

        validated.append(
            {
                "question":
                    question_text.strip(),

                "options":
                    cleaned_options,

                "answer":
                    cleaned_answer,
            }
        )

    return validated


def generate_quiz(text: str) -> list[dict]:
    """
    Generate exactly three MCQs
    from the supplied educational text.
    """

    if not text or not text.strip():
        raise ValueError(
            "Text cannot be empty."
        )

    prompt = f"""
Create exactly 3 multiple-choice questions
from the educational content below.

CONTENT:
{text}

Return ONLY valid JSON.

Required JSON structure:

[
  {{
    "question": "Question text",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer": "Correct option text"
  }}
]

Rules:
- Exactly 3 questions.
- Exactly 4 options per question.
- Exactly one correct answer.
- The answer must exactly match one of the options.
- Questions must be based only on the supplied content.
- Make the questions educational and meaningful.
- Do not include Markdown.
- Do not include explanations outside the JSON.
"""

    response = generate_text(
        prompt,
        system_instruction=(
            "You generate structured educational "
            "multiple-choice questions and must "
            "return valid JSON."
        ),
    )

    cleaned = clean_json_block(
        response
    )

    try:

        data = json.loads(
            cleaned
        )

    except json.JSONDecodeError as exc:

        raise ValueError(
            "Gemini returned invalid JSON for the quiz."
        ) from exc

    return _validate_quiz(data)