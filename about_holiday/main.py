from fastapi import FastAPI

from about_holiday.see_holiday.router import router

app = FastAPI()


@app.get("/")
def get():
    return 'Success'

app.include_router(router)
