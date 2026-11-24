import pytest

from app.services.job_service import clear_jobs


@pytest.fixture(autouse=True)
def reset_jobs():
    clear_jobs()
    yield
    clear_jobs()