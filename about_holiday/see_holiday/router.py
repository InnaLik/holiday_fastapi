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


@router.get("/month/")
async def get_holiday_month(id_m: int, sessions: AsyncSession = Depends(get_async_session)):
    query = select(Holiday).where(Holiday.id_month == id_m).order_by(Holiday.id_day)
    result = await sessions.execute(query)
    return {"status": "success",
            "result": result.mappings().all()}


@router.get("/{month}/{day}/")
async def get_holiday_month(month: int, day: int, sessions: AsyncSession = Depends(get_async_session)):
    query = select(Holiday).where(Holiday.id_month == month).where(Holiday.id_day == day).order_by(Holiday.id_day)
    result = await sessions.execute(query)
    return {"status": "success",
            "result": result.mappings().all()}
