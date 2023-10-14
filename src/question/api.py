import os
import asyncio
from httpx import AsyncClient, HTTPStatusError, TimeoutException

from fastapi import HTTPException


async def request(client: AsyncClient, count: int):
    """Request API"""
    try:
        url = os.environ.get('URL_API')
        response = await client.get(f'{url}/random?count={count}')
        response.raise_for_status()
        return response.json()
    except TimeoutException:
        raise HTTPException(
            status_code=504,
            detail='The operation timed out while requesting the API https://jservice.io/api.'
        )
    except HTTPStatusError:
        raise HTTPException(
            status_code=500,
            detail='Error sending request to API https://jservice.io/api'
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=exc)


async def get_data_request(questions_num: int):
    """Run Async task"""
    async with AsyncClient() as client:
        task = request(client, questions_num)
        result = await asyncio.gather(task)
        return result[0]
