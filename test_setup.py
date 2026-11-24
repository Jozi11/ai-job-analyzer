from pydantic import BaseModel
from fastapi import FastAPI


class Job(BaseModel):
    title: str
    required_skills: list[str]


job = Job(
    title="Junior Data Analyst",
    required_skills=["Python", "SQL", "Statistics"]
)

print(job.model_dump())

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Job Analyzer is running!"}