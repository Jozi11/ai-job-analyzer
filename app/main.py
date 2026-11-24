from fastapi import FastAPI

from app.models.job import Job
from app.services import job_service

app = FastAPI(
    title="AI Job Analyzer",
    description="An application for CV analysis and job matching",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Job Analyzer",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/jobs")
def create_job(job: Job):
    job_service.add_job(job)
    return {
        "message": "Job successfully created",
        "job": job
    }


@app.get("/jobs")
def get_jobs():
    return job_service.get_all_jobs()