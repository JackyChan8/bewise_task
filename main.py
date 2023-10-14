from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel.ext.asyncio.session import AsyncSession

from core.db import init_db, get_session
from src.question.api import get_data_request
from src.question.schemas import QuestionNumber
from src.question.models import Questions, QuestionBase
from src.question.services import get_last_question, create_questions, check_exists

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/questions')
async def get_question(data: QuestionNumber, session: AsyncSession = Depends(get_session)):
    # Запроса на Сервис
    questions = await get_data_request(data.questions_num)
    # Получение последнего вопроса
    last_question = await get_last_question(session)
    # Проверка на существования вопроса
    data, count = await check_exists(session, questions)
    # Цикл запускается если есть существующие в базе вопросы
    while count:
        new_questions = await get_data_request(count)
        new_data, new_count = await check_exists(session, new_questions)
        count = new_count
        data = data + new_data
    # Сохранение в базу данных
    await create_questions(session, data)
    if not last_question:
        return {}
    else:
        return last_question
