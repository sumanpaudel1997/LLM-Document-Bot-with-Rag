import os
import logging

from llama_index.llms.openai import OpenAI
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core import Settings
from dotenv import load_dotenv
load_dotenv()

# utility functions
from utils.data_ingestion import load_documents
from utils.qdrant_db import qdrant_vector_db
from utils.vector_index import vector_index


logging.basicConfig(
                    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(message)s"
                    ,level=logging.INFO,
                    filename="llm.log",
                    filemode="w")

FILE_PATH = './data/docs/'

# OPENAI Configuration
api_key = os.getenv('OPENAI_API_KEY') #use your own api key to access LLM
os.environ['OPENAI_API_KEY'] = api_key
llm = OpenAI()
Settings.llm = llm

# Hugging Face Embedding
# produces embeddings 384 wide, at float32 that equals 1536 bytes each.
# The size of all the vectors for 100 items is 153kb. 

Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# set memory buffer for chat conversation history, for now the token limit is 3900.
# can be increased as per need
memory = ChatMemoryBuffer.from_defaults(token_limit=3900)

def main():
    
    #ingest the documents
    logging.info('Ingesting The Data.') #log the ingestion
    documents = load_documents(FILE_PATH)
    
    # qdrant client and vector store
    logging.info("Connecting to Qdrant Instance") #log the instance connection and creation
    vector_store =qdrant_vector_db()
    
    # get the vector index
    logging.info("Creating the Vector indices") #log the creation of vection indices
    index = vector_index(vector_store=vector_store, data_loader=documents)
    
    
    # create a chat engine that will take the prompt
    logging.info('Creating Chat Engine')
    chat_engine = index.as_chat_engine(
                    chat_mode='context',
                    memory=memory,
                    system_prompt=(
                    "You are a chatbot, able to have normal interactions with previous conversations, as well as talk"
                    " Help to generate the given query prompt \n{query}"
                    "Don't use your knowledge except for the context"),
                    verbose=True,
                    )
    
    logging.info("All OK.")
    #ask the user for Input prompt
    counter = 0
    while True:
        query = input("\nAsk your Question: ")
        res = chat_engine.chat(query)
        history = [(query,res)]
        logging.info(history)
        print(f"\nResponse: \n\n{res}\n\nThank you\n" + '*'*130 + '\n')
        counter += 1
        if counter == 5:
            print("Query Prompting Limit Reached. Max 5 queries per session.")
            break
        
        
if __name__ == '__main__':
    
    print('The data is pdf file of research paper "Attention is All you need".')
    main()