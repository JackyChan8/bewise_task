from pydantic import BaseModel


class QuestionNumber(BaseModel):
    questions_num: int
