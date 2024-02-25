# LLM Document CLI Bot with Rag

A cli based chatbot which helps in reading the context of given documents (PDF)

## Installation

To get started, follow these steps:

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the application with `python main.py`.

## Usage

- Use the app to do something query the pdf file !
- The app understands the context you are providing with respect to pdf file

## Folder Structure
- **data**: This directory contains all the data files required for the project. 
- **qdrant**: A folder containing qdrant local instance to save the vector emebeddings.
- **utils**: A directory containing utility scripts that are used across the project.
    - `vector_index.py`: Used for creating and managing vector indices.
    - `data_ingestion.py`: This script is used for ingesting data into the application.
    - `qdrant_db.py`: Handles operations related to 'qdrant' database.
- **vector_index**: Folder containing files that stores storage context container which is a utility container for storing nodes, indices, and vectors.
- `requirement.txt` : all of the dependencies needed to run the project.
- `Dockerfile` : Contains dockerized version of application
- `.gitignore` : Contains list of the files that are ignored while pushing. e.g .env file, log files 


