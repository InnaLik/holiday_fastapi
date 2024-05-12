from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from about_holiday.database import get_async_session
from about_holiday.see_holiday.models import Holiday

router = APIRouter(prefix='/holiday',
                   tags=['Get_Holiday'])

@router.get("/")
async def get_holiday(sessions: AsyncSession = Depends(get_async_session)):
    query = select(Holiday)
    result = await sessions.execute(query)
    return result.mappings().all()

