from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import ComplaintsTable
from sqlalchemy import create_engine, select
from typing import Optional

engine = create_engine("postgresql://postgres:changeme@localhost:5432")

app = FastAPI(
    title="FastAPI-SQLAlchemy",
    description="A simple FastAPI + SQLAlchemy example",
    version="0.1.0",
)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint

    Parameters
    ----------
    None

    Returns
    -------
    dict
        A dict with a welcome message

    """
    return {"Hello": "Welcome to the FastAPI-SQLAlchemy API"}


@app.get("/complaints", tags=["Complaints"])
async def get_complaints(limit: Optional[int] = None):
    """Get all complaints

    Parameters
    ----------
    limit : int, optional
        Limit the number of complaints returned, by default None

    Returns
    -------
    list
        A list of dicts with all complaints

    """
    with engine.connect() as conn:
        if limit:
            query = select(ComplaintsTable).limit(limit)
        else:
            query = select(ComplaintsTable)
        result = conn.execute(query)
        # create a list of dicts from the result zipping the keys and values
        return [dict(zip(result.keys(), row)) for row in result.fetchall()]
