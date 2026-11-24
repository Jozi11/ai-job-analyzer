from app.models.job import Job

_jobs: list[Job] = []


def add_job(job: Job) -> Job:
    _jobs.append(job)
    return job


def get_all_jobs() -> list[Job]:
    return list(_jobs)


def clear_jobs() -> None:
    _jobs.clear()