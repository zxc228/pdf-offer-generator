from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from routes import service_routes, pdf_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db() 

app.include_router(service_routes.router)
app.include_router(pdf_routes.router)

@app.get("/")
def root():
    return {"message": "PDF Generator API is running"}
