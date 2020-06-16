from basilica import Connection
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("BASILICA_API_KEY") #Use env var


# could use a function here to return the connection
# could use a class


connection = Connection(API_KEY)
print("CONNECTION", type(connection))


if __name__ == "__main__":

    sentences = [
        "This is a sentence!",
        "This is a similar sentence!",
        "I don't think this sentence is very similar at all...",
    ]

    embeddings = list(connection.embed_sentences(sentences))


    print(embeddings)
    # Check the length, the type, the class of this embedding.
    print(type(embedding)) - # object is list
    print(type(embedding[0])) - # float class
    print(len(embeddings)) - # Length of 768
