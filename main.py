from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from routes import router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔹 Permitir cualquier origen (ÚSALO SOLO EN DESARROLLO)
    allow_credentials=True,
    allow_methods=["*"],  # 🔹 Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # 🔹 Permitir todos los headers
)

app.include_router(router)




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
ç