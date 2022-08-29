from fastapi import FastAPI
from starlette.responses import RedirectResponse

#config file
from app.core.config import Settings

#databse
import app.database.models as models
from app.database.dbConfig import engine

#routing
from app.api.myApi import router as apiRouter


# app is instance of the class FastAPI 
app = FastAPI(title=Settings.PROJECT_NAME,version=Settings.PROJECT_VERSION)


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


models.Base.metadata.create_all(bind=engine)

#router for different api
app.include_router(apiRouter)
