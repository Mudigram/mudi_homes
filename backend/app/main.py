from fastapi import FastAPI
from app.routers import blogs as blog_router
from app.routers import listings as listing_router
from app.routers import users as user_router
from app.database import Base, engine

# create tables in dev (Alembic will be used for prod migrations)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mudi Homes API")

@app.get("/ping")
def ping():
    return {"ping": True}


app.include_router(blog_router.router)
app.include_router(listing_router.router)
app.include_router(user_router.router)
