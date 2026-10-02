from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from explanation_module import explain_topic
from learning_path import get_learning_recommendations
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text


BASE_DIR = Path(__file__).resolve().parent


app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0",
)


app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)


templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)


class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="Input text or question",
    )


class ExplanationRequest(BaseModel):
    topic: str = Field(
        ...,
        min_length=1,
        description="Topic to explain",
    )


class LearningPathRequest(BaseModel):
    topic: str = Field(
        ...,
        min_length=1,
        description="Topic to learn",
    )

    level: str = Field(
        default="beginner",
        min_length=1,
        description="Learner level",
    )


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "application": "EduGenie",
    }


@app.post("/qa")
async def qa(request: TextRequest):
    try:
        result = answer_question(request.text)

        return {
            "success": True,
            "result": result,
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )


@app.post("/explain")
async def explain(request: ExplanationRequest):
    try:
        result = explain_topic(request.topic)

        return {
            "success": True,
            "result": result,
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )


@app.post("/quiz")
async def quiz(request: TextRequest):
    try:
        result = generate_quiz(request.text)

        return {
            "success": True,
            "quiz": result,
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )


@app.post("/summarize")
async def summarize(request: TextRequest):
    try:
        result = summarize_text(request.text)

        return {
            "success": True,
            "result": result,
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )


@app.post("/learn/recommendations")
async def learning_recommendations(
    request: LearningPathRequest,
):
    try:
        result = get_learning_recommendations(
            topic=request.topic,
            level=request.level,
        )

        return {
            "success": True,
            "result": result,
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )