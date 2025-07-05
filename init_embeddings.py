import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus

from embedding import split_to_chunks, generate_embeddings

load_dotenv()

async def create_save_embeddings():
    DATASET_URL = "https://github.com/GoogleCloudPlatform/python-docs-samples/raw/main/cloud-sql/postgres/pgvector/data/retail_toy_dataset.csv"
    df = pd.read_csv(DATASET_URL)

    chunked = split_to_chunks(dataframe=df)
    batch_size = 100
    print(f"Total size: { len(chunked)} | Batch size: { batch_size} | no of batches: { len(chunked)//batch_size }")
    for i in range(0, len(chunked), batch_size):
        request = [x["content"] for x in chunked[i : i + batch_size]]
        print(f"processing batch: {i}")
        response = await generate_embeddings(request)
        # Store the retrieved vector embeddings for each chunk back.
        for x, e in zip(chunked[i : i + batch_size], response):
            x["embedding"] = e
    df_embeddings = pd.DataFrame(chunked)
    print(df_embeddings)
    print('storing embeddings')
    engine = create_engine(f"postgresql://{os.getenv("POSTGRES_USER")}:{quote_plus(os.getenv("POSTGRES_PASSWORD"))}@{os.getenv("POSTGRES_SERVER")}:{os.getenv("POSTGRES_PORT")}/{os.getenv("POSTGRES_DATABASE")}")
    df_embeddings.to_sql('product_embeddings', con=engine, if_exists='append', index=False)
    print('stored')
    return None