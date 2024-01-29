from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import psycopg2

connection = psycopg2.connect(
    user="postgres",
    password="changeme",
    host="localhost",
    port="5432",
    database="postgres",
)

app = FastAPI(
    title="FastAPI-Psycopg2",
    description="A simple FastAPI + Psycopg2 example",
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
    return {"Hello": "Welcome to the FastAPI-Psycopg2 API"}


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
    with connection.cursor() as cursor:
        if limit:
            cursor.execute(
                "SELECT * FROM complaints_table LIMIT %s", (limit,)
            )
        else:
            cursor.execute("SELECT * FROM complaints_table")
        # get list of column names
        columns = [desc[0] for desc in cursor.description]
        # get list of results
        result = cursor.fetchall()
        # create a list of dicts from the result zipping the keys and values
        return [dict(zip(columns, row)) for row in result]
