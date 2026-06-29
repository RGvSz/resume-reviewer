from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from groq import Groq
import os
import json

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "your_groq_api_key_here")

class ReviewRequest(BaseModel):
    resume: str
    job_description: str

@app.get("/")
def read_root():
    return FileResponse("static/index.html")

@app.post("/review")
def review_resume(request: ReviewRequest):
    if not request.resume.strip() or not request.job_description.strip():
        raise HTTPException(status_code=400, detail="Resume and job description are required")

    client = Groq(api_key=GROQ_API_KEY)

    prompt = f"""You are an expert resume coach and ATS (Applicant Tracking System) specialist.

Analyze the following resume against the job description and provide a detailed review.

RESUME:
{request.resume}

JOB DESCRIPTION:
{request.job_description}

Respond ONLY with a valid JSON object in this exact format (no markdown, no explanation outside JSON):
{{
  "match_score": <number 0-100>,
  "summary": "<2-3 sentence overall assessment>",
  "strengths": ["<strength 1>", "<strength 2>", "<strength 3>"],
  "missing_keywords": ["<keyword 1>", "<keyword 2>", "<keyword 3>", "<keyword 4>", "<keyword 5>"],
  "weaknesses": ["<weakness 1>", "<weakness 2>", "<weakness 3>"],
  "improved_bullets": [
    {{"original": "<original bullet point>", "improved": "<improved version>"}},
    {{"original": "<original bullet point>", "improved": "<improved version>"}}
  ],
  "top_suggestions": ["<suggestion 1>", "<suggestion 2>", "<suggestion 3>"]
}}"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500,
        temperature=0.3
    )

    try:
        text = response.choices[0].message.content
        # Strip markdown code fences if present
        text = text.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        result = json.loads(text)
        return result
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Failed to parse AI response")
