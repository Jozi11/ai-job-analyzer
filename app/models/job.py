from pydantic import BaseModel, Field


class Job(BaseModel):
    title: str = Field(min_length=2)
    company: str = Field(min_length=2)
    description: str = Field(min_length=20)
    required_skills: list[str] = Field(default_factory=list)