from pydantic import BaseModel, Field


class AddHoliday(BaseModel):
    id: int
    title: str
    description: str
    slug: str
    id_month: int
    id_day: int
