import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:K130309980@localhost:5432/WeShop"
)

try:
    with engine.connect() as conn:
        print("Connected successfully")

    df = pd.read_sql("SELECT * FROM categories", engine)

    print(df)

except Exception as e:
    print("Error:", e)