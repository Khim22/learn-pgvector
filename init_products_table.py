import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

def init_products():
    print('init')
    DATASET_URL = "https://github.com/GoogleCloudPlatform/python-docs-samples/raw/main/cloud-sql/postgres/pgvector/data/retail_toy_dataset.csv"
    df = pd.read_csv(DATASET_URL)
    df = df.loc[:, ["product_id", "product_name", "description", "list_price"]]
    df = df.dropna()
    print(df.head(10))

    print('create_engine')
    print()
    # Format: postgresql://username:password@localhost:port/database
    engine = create_engine(f"postgresql://{os.getenv("POSTGRES_USER")}:{quote_plus(os.getenv("POSTGRES_PASSWORD"))}@{os.getenv("POSTGRES_SERVER")}:{os.getenv("POSTGRES_PORT")}/{os.getenv("POSTGRES_DATABASE")}")

    print('insert')
    df.to_sql("products", engine, if_exists="append", index=False)


