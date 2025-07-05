import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings

load_dotenv()

def split_to_chunks(dataframe):
    df = dataframe
    text_splitter = RecursiveCharacterTextSplitter(
        separators=[".", "\n"],
        chunk_size=500,
        chunk_overlap=80,
        length_function=len,
    )
    chunked = []
    df.dropna(subset=['description'], inplace=True)
    
    for index, row in df.iterrows():
        product_id = row["product_id"]
        desc = row["description"]
        # print('ffffffffffffffff',[desc])
        splits = text_splitter.create_documents([desc])
        for s in splits:
            r = {"product_id": product_id, "content": s.page_content}
            chunked.append(r)
    
    return chunked

async def generate_embeddings(texts):
    # Specify the embedding model
    model = "sentence-transformers/all-mpnet-base-v2" 
    try:
        embeddings = HuggingFaceEndpointEmbeddings(
            huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
            model=model
        )
        vector = await embeddings.aembed_documents(texts)

        return vector
    except Exception as e:
        print(f"Error generating embeddings: {e}")
        return None