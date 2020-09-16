from basilica import Connection
import os
from dotenv import load_dotenv 

load_dotenv()
API_KEY = os.getenv("BASILICA_API_KEY")

connection = Connection(API_KEY) 
print("connection", type(connection))  

if __name__ == "__main__":

    sentences = [
            "This is a sentence!"
            "This is a similar sentence"
            "I don't think this sentence is very similar at all..."
    ]

    connection = Connection(API_KEY) 
    print("connection", type(connection))  

    embeddings = list(connection.embed_sentences(sentences))
    print(embeddings)

    embedding = list(connection.embed_sentences('Hello World!'))
    print(embedding)