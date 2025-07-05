
import asyncio

import embedding
from init_products_table import init_products
from init_embeddings import create_save_embeddings

from sqlalchemy import text


async def main():
    print('hello')
    # init_products()
    # await create_save_embeddings()
    toy = "play card games"  # @param {type:"string"}
    min_price = 20  # @param {type:"integer"}
    max_price = 200  # @param {type:"integer"}

    # test_query = text("""
    #     WITH vector_matches AS (
    #         SELECT product_id, 1 - (embedding <=> :embedded_query) AS similarity
    #         FROM product_embeddings
    #         WHERE 1 - (embedding <=> :embedded_query) > :similarity_threshold
    #         ORDER BY similarity DESC
    #         LIMIT :num_matches
    #     )
    #     SELECT product_name, list_price, description FROM products
    #     WHERE product_id IN (SELECT product_id FROM vector_matches)
    #     AND list_price >= :min_price AND list_price <= :max_price
    # """)


    

    # embeddings = generate_embeddings(chunked[0]["content"])
    # print(embeddings)
if __name__ == "__main__":
    asyncio.run(main())