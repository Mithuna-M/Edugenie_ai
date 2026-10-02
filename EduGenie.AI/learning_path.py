from gemini_client import generate_text


def get_learning_recommendations(
    topic: str,
    level: str = "beginner",
) -> str:
    """
    Generate a structured learning path
    for a given topic and learner level.
    """

    if not topic or not topic.strip():
        raise ValueError(
            "Topic cannot be empty."
        )

    level = level.strip() or "beginner"

    prompt = f"""
Create a personalized learning path for:

Topic:
{topic}

Learner level:
{level}

Create a progression from beginner to advanced.

Include:

1. Learning goal
2. Prerequisites
3. Beginner stage
4. Intermediate stage
5. Advanced stage
6. Suggested timeline
7. Practice activities
8. Project ideas
9. Recommended resources

For each stage:
- Explain what to learn.
- Explain why it matters.
- Give practical activities.

Resources may include:
- Official documentation
- Books
- Articles
- Videos
- Practice websites

Keep the plan realistic and student-friendly.
"""

    return generate_text(
        prompt,
        system_instruction=(
            "You are an educational mentor who creates "
            "structured and practical learning paths."
        ),
    )