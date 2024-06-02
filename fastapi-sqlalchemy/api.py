from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from models import ComplaintsTable, PriceTable
from sqlalchemy import create_engine, select, insert, delete
from typing import Optional

# localhost if running from command line
# engine = create_engine("postgresql://postgres:changeme@localhost:5433")
# postgres if running from docker-compose
engine = create_engine("postgresql://postgres:changeme@postgres:5432")

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
    with engine.begin() as conn:
        if limit:
            query = select(ComplaintsTable).limit(limit)
        else:
            query = select(ComplaintsTable)
        result = conn.execute(query)
        # create a list of dicts from the result zipping the keys and values
        return [dict(zip(result.keys(), row)) for row in result.fetchall()]


@app.get("/complaints/{complaint_id}", tags=["Complaints"])
async def get_complaint(complaint_id: int):
    """Get a single complaint

    Parameters
    ----------
    complaint_id : int
        The complaint id

    Returns
    -------
    dict
        A dict with the complaint

    """
    with engine.begin() as conn:
        query = select(ComplaintsTable).where(
            ComplaintsTable.complaint_id == complaint_id
        )
        result = conn.execute(query)
        return dict(zip(result.keys(), result.fetchone()))


@app.get("/prices", tags=["Prices"])
async def get_prices(limit: Optional[int] = None):
    """Get all prices

    Parameters
    ----------
    limit : int, optional
        Limit the number of prices returned, by default None

    Returns
    -------
    list
        A list of dicts with all prices

    """
    with engine.begin() as conn:
        if limit:
            query = select(PriceTable).limit(limit)
        else:
            query = select(PriceTable)
        result = conn.execute(query)
        return [dict(zip(result.keys(), row)) for row in result.fetchall()]


@app.get("/prices/{complaint_id}", tags=["Prices"])
async def get_price(complaint_id: int):
    """Get a single price

    Parameters
    ----------
    complaint_id : int
        The complaint id

    Returns
    -------
    dict
        A dict with the price

    """
    with engine.begin() as conn:
        query = select(PriceTable).where(
            PriceTable.complaint_id == complaint_id
        )
        result = conn.execute(query)
        return dict(zip(result.keys(), result.fetchone()))


@app.get("/complaints/{complaint_id}/price", tags=["Complaints"])
async def get_complaint_price(complaint_id: int):
    """Get a single complaint with price

    Parameters
    ----------
    complaint_id : int
        The complaint id

    Returns
    -------
    dict
        A dict with the complaint and price

    """
    with engine.begin() as conn:
        query = (
            select(ComplaintsTable)
            .where(ComplaintsTable.complaint_id == complaint_id)
            .join(
                PriceTable,
                onclause=ComplaintsTable.complaint_id
                == PriceTable.complaint_id,
            )
        )
        result = conn.execute(query)
        return dict(zip(result.keys(), result.fetchone()))


@app.get("/complaints/price/all", tags=["Complaints"])
def get_all_complaints_prices():
    """Get all complaints with prices

    Parameters
    ----------
    None

    Returns
    -------
    list
        A list of dicts with all complaints and prices

    """
    with engine.begin() as conn:
        query = select(ComplaintsTable).join(
            PriceTable,
            onclause=ComplaintsTable.complaint_id == PriceTable.complaint_id,
        )
        result = conn.execute(query)
        return [dict(zip(result.keys(), row)) for row in result.fetchall()]


@app.post("/prices", tags=["Prices"])
async def create_price(complaint_id: int, price: int):
    """Create a new price

    Parameters
    ----------
    complaint_id : int
        The complaint id
    price : PriceTable
        The price to create

    Returns
    -------
    dict
        A dict with the created price

    """
    with engine.begin() as conn:
        query = (
            insert(PriceTable)
            .values({"complaint_id": complaint_id, "price": price})
            .returning(PriceTable.complaint_id)
        )
        result = conn.execute(query)
        return {"complaint_id": result.fetchone()[0], "price": price}


@app.get("/complaints/date_received/{date_received}", tags=["Complaints"])
async def get_complaints_by_date(date_received: str):
    """Get all complaints by date received

    Parameters
    ----------
    date_received : str
        The date received

    Returns
    -------
    list
        A list of dicts with all complaints by date received

    """
    with engine.begin() as conn:
        query = select(ComplaintsTable).where(
            ComplaintsTable.date_received == date_received
        )
        result = conn.execute(query)
        return [dict(zip(result.keys(), row)) for row in result.fetchall()]


@app.delete("/complaints/{complaint_id}", tags=["Complaints"])
async def delete_complaint(complaint_id: int):
    """Delete a single complaint

    Parameters
    ----------
    complaint_id : int
        The complaint id

    Returns
    -------
    dict
        A dict with the complaint

    """
    with engine.begin() as conn:
        query = ComplaintsTable.delete().where(
            ComplaintsTable.complaint_id == complaint_id
        )
        _ = conn.execute(query)
        return {"complaint_id": complaint_id, "status": "deleted"}


@app.delete("/prices/{complaint_id}", tags=["Prices"])
async def delete_price(complaint_id: int):
    """Delete a single price

    Parameters
    ----------
    complaint_id : int
        The complaint id

    Returns
    -------
    dict
        A dict with the price

    """
    with engine.begin() as conn:
        query = delete(PriceTable).where(
            PriceTable.complaint_id == complaint_id
        )
        _ = conn.execute(query)
        return {"complaint_id": complaint_id, "status": "deleted"}
