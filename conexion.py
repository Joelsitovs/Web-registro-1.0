import os
import dotenv
from google.cloud import firestore


dotenv.load_dotenv()

name_db = os.getenv("NAME_DB")

db = firestore.Client(database=name_db)

print("Firestore conectado correctamente")

__all__ = ["db"]
