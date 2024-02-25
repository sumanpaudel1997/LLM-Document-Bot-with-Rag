from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI

import os

api_key = os.getenv('OPENAI_API_KEY')
# Necessary to use the latest OpenAI models that support function calling API
llm = OpenAI(model="gpt-3.5-turbo",api_key=api_key)
data = SimpleDirectoryReader("./data/docs/").load_data()
index = VectorStoreIndex.from_documents(data)

chat_engine = index.as_chat_engine(chat_mode="openai", llm=llm, verbose=True)
response = chat_engine.chat("Hi")
print(response)