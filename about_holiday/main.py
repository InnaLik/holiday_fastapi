import aioredis
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from about_holiday.see_holiday.router import router

app = FastAPI()


@app.get("/")
def get():
    return 'Success'

app.include_router(router)

# подключение к бд редис
@app.on_event("startup")
async def startup_event():
    # идет подключение к редису
    redis = aioredis.from_url("redis://127.0.0.1:6379", encoding="utf8", decode_responces=True)
    # инициализация класса, после этого можем использовать декоратор cache(expire=30) и сколько секунд
    # будет храниться кэш
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")