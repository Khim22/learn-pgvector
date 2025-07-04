import pandas as pd
import os

def main():
    print('hello')


    DATASET_URL = "https://github.com/GoogleCloudPlatform/python-docs-samples/raw/main/cloud-sql/postgres/pgvector/data/retail_toy_dataset.csv"
    df = pd.read_csv(DATASET_URL)
    df = df.loc[:, ["product_id", "product_name", "description", "list_price"]]
    df = df.dropna()
    print(df.head(10))

if __name__ == "__main__":
    main()