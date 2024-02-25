from llama_index.core import PromptTemplate
sample = (
    "Please write a passage to answer the question\n"
    "Try to include as many key details as possible.\n"
    "Do not try to answer on your own using prior knowledge"
    "\n"
    "\n"
    "{query_str}\n"
    "\n"
    "\n"
    'Thank You !! \n'
)

prompt_template = PromptTemplate(sample)
print(prompt_template)