from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os
from fastapi.middleware.cors import CORSMiddleware
import csv
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

# Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please create a .env file with your OpenAI API key.")
client = OpenAI(api_key=api_key)

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerationRequest(BaseModel):
    platform: str
    tone: str
    type: str
    audience: str
    goal: str
    topic: str

class FeedbackRequest(BaseModel):
    post: str
    feedback: str

prompt_templates = {
    "LinkedIn": """You are a professional content writer for LinkedIn. Write a {tone} {type} targeted at {audience}. Goal: {goal}.

Topic: {topic}

Guidelines:
- Format: Hook + value + reflection + CTA
- Length: Max 1300 characters
- Include 2–3 relevant hashtags and a question at the end
""",
    "X": """You are a social media writer for X (Twitter). Write a {tone} {type}. Goal: {goal}.

Topic: {topic}

Guidelines:
- Length: 280 characters (or thread with 3–6 tweets if type=thread)
- Include emojis and trending hashtags
- Start with a strong hook
"""
}

@app.post("/generate")
async def generate_post(data: GenerationRequest):
    try:
        prompt = prompt_templates[data.platform].format(
            tone=data.tone,
            type=data.type,
            audience=data.audience,
            goal=data.goal,
            topic=data.topic
        )
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=500
        )
        post_content = response.choices[0].message.content

        # Log data to CSV
        try:
            with open("feedback.csv", "a", newline="", encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([
                    datetime.now(), data.platform, data.tone, data.type, data.audience, data.goal, data.topic, post_content
                ])
        except Exception as e:
            print(f"Error writing to CSV: {e}")

        return {"post": post_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/feedback")
async def collect_feedback(data: FeedbackRequest):
    try:
        with open("feedback.csv", "a", newline="", encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), "FEEDBACK", "", "", "", "", "", data.post, data.feedback])
        return {"message": "Feedback recorded"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 