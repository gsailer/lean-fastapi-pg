from fastapi import FastAPI

from .example import router as examples

app = FastAPI()


@app.get("/healthz")
async def healthz():
    return {"api": True}


app.include_router(examples.router, prefix="/example", tags=["examples"])
