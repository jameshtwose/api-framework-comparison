# %%
from sqlalchemy import create_engine, text, select
import pandas as pd
from models import ComplaintsTable, PriceTable
import numpy as np

# %%
engine = create_engine("postgresql://postgres:changeme@localhost:5433")

# %%
with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())
    conn.commit()
# %%
# load in the complaints data
amount_of_rows = 100000
pre_df = pd.read_csv(
    "data/complaints.csv",
    nrows=amount_of_rows,
)
pre_df.columns = (
    pre_df.columns.str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
    .str.replace("?", "")
)
pre_df.shape

# %%
df = pre_df.assign(
    **{
        "date_received": pd.to_datetime(pre_df["date_received"]),
        "date_sent_to_company": pd.to_datetime(
            pre_df["date_sent_to_company"]
        ),
    }
)
# %%
df.head()
# %%
df.info()
# %%
try:
    ComplaintsTable.__table__.create(engine)
    PriceTable.__table__.create(engine)
except Exception as e:
    print(e)
# %%
with engine.begin() as conn:
    df.to_sql(
        "complaints_table",
        conn,
        if_exists="replace",
        index=False,
        chunksize=1000,
    )
# %%
with engine.begin() as conn:
    query = select(ComplaintsTable).limit(5)
    result = conn.execute(query)
    sql_df = pd.DataFrame(result.fetchall())
# %%
with engine.begin() as conn:
    query = (
        select(ComplaintsTable)
        .where(
            ComplaintsTable.date_received
            > pd.Timestamp.now() - pd.Timedelta(days=200)
        )
        .order_by(ComplaintsTable.date_received.desc())
    )
    result = conn.execute(query)
    sql_df = pd.DataFrame(result.fetchall())
print(sql_df.shape)

# %%
price_df = pd.DataFrame(
    {
        "complaint_id": df["complaint_id"],
        "price": np.random.uniform(0, 100, size=amount_of_rows).round(2),
    }
)

with engine.begin() as conn:
    price_df.to_sql(
        "price_table",
        conn,
        if_exists="replace",
        index=False,
        chunksize=1000,
    )

# %%
# drop the table
# ComplaintsTable.__table__.drop(engine)
# PriceTable.__table__.drop(engine)
# %%
