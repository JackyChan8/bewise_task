from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc, col

from src.question.models import Questions


async def get_last_question(session: AsyncSession):
    """Get last Question"""
    try:
        statement = select(Questions.question) \
            .order_by(desc(Questions.id)) \
            .limit(1)
        result = await session.exec(statement)
        return result.first()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=exc)


async def check_exists(session: AsyncSession, data):
    """Check exists questions"""
    try:
        ids_question = [el['id'] for el in data]
        statement = select(Questions.question_id) \
            .where(col(Questions.question_id).in_(ids_question))
        result = await session.exec(statement)
        exists_elements = result.all()
        if len(exists_elements) > 0:
            # Фильтрация данных
            new_data = list(filter(lambda x: x['id'] not in exists_elements, data))
            return new_data, len(exists_elements)
        else:
            return data, len(exists_elements)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=exc)


async def create_questions(session: AsyncSession, data):
    """Insert question to Database"""
    try:
        questions = [
            Questions(
                question_id=el['id'],
                answer=el['answer'],
                question=el['question'],
            ) for el in data
        ]
        for question in questions:
            session.add(question)

        await session.commit()
        await session.close()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=exc)
