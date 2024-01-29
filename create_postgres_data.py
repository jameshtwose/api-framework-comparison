# %%
from sqlalchemy import create_engine, text, select
import pandas as pd
from models import ComplaintsTable

# %%
engine = create_engine("postgresql://postgres:changeme@localhost:5432")

# %%
with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())
    conn.commit()
# %%
# load in the complaints data
pre_df = pd.read_csv(
    "data/complaints.csv",
    nrows=100000,
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
except Exception as e:
    print(e)
# %%
with engine.connect() as conn:
    df.to_sql(
        "complaints_table",
        conn,
        if_exists="replace",
        index=False,
        chunksize=1000,
    )
# %%
with engine.connect() as conn:
    query = select(ComplaintsTable).limit(5)
    result = conn.execute(query)
    sql_df = pd.DataFrame(result.fetchall())
# %%
with engine.connect() as conn:
    query = (
        select(ComplaintsTable)
        .where(
            ComplaintsTable.date_received
            > pd.Timestamp.now() - pd.Timedelta(days=30)
        )
        .order_by(ComplaintsTable.date_received.desc())
    )
    result = conn.execute(query)
    sql_df = pd.DataFrame(result.fetchall())
print(sql_df.shape)

# %%
# drop the table
ComplaintsTable.__table__.drop(engine)
# %%
