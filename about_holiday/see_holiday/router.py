from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from about_holiday.database import get_async_session
from about_holiday.see_holiday.models import Holiday
from about_holiday.see_holiday.schema import AddHoliday

router = APIRouter(prefix='/holiday',
                   tags=['Get_Holiday'])

@router.get("/")
async def get_holiday(sessions: AsyncSession = Depends(get_async_session)):
    query = select(Holiday)
    result = await sessions.execute(query)
    return result.mappings().all()

@router.post("/")
async def add_holiday(holiday: AddHoliday, sessions: AsyncSession = Depends(get_async_session)):
    stmt = insert(Holiday).values(**holiday.dict())
    await sessions.execute(stmt)
    await sessions.commit()
    return {"status": "success"}