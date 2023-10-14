from sqlmodel import SQLModel, Field
from datetime import datetime


class QuestionBase(SQLModel):
    question_id: int = Field(nullable=False)
    answer: str = Field(max_length=255, nullable=False)
    question: str = Field(nullable=False, unique=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class Questions(QuestionBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
