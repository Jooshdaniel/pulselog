from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="PulseLog")

app.include_router(router)
