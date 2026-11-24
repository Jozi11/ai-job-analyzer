from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_create_job():
    job_data = {
        "title": "Junior Data Analyst",
        "company": "Example GmbH",
        "description": "Looking for someone with Python and SQL experience.",
        "required_skills": ["Python", "SQL"]
    }

    response = client.post("/jobs", json=job_data)

    assert response.status_code == 200
    assert response.json()["job"]["title"] == "Junior Data Analyst"


def test_invalid_job():
    job_data = {
        "title": "A",
        "company": "X",
        "description": "Short"
    }

    response = client.post("/jobs", json=job_data)

    assert response.status_code == 422


def test_get_jobs():
    
    response = client.get("/jobs")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_jobs_returns_created_job():
    job_data = {
        "title": "Junior Data Analyst",
        "company": "Example GmbH",
        "description": "Looking for someone with Python and SQL experience.",
        "required_skills": ["Python", "SQL"]
    }

    post_response = client.post("/jobs", json=job_data)
    assert post_response.status_code == 200

    response = client.get("/jobs")

    assert response.status_code == 200
    result = response.json()
    assert len(result) == 1
    assert result[0]["title"] == "Junior Data Analyst"