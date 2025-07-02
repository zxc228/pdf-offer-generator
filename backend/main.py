from fastapi import FastAPI
from database import init_db
from routes import service_routes, pdf_routes

app = FastAPI()

init_db() 

app.include_router(service_routes.router)
app.include_router(pdf_routes.router)

@app.get("/")
def root():
    return {"message": "PDF Generator API is running"}
