from application.routes import quiz_route

from fastapi import FastAPI

app = FastAPI()

app.include_router(quiz_route.router)
