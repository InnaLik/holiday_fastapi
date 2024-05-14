from pydantic import BaseModel, Field


class Monthes(BaseModel):
    id: int
    title: str
    count_days: int


class Days(BaseModel):
    id: int


class AddHoliday(BaseModel):
    id: int
    title: str
    description: str
    slug: str
    id_month: int
    id_day: int
