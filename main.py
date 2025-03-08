from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://erp-platform-2qfpo5do7-matricsquantums-projects.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Hello from ERP Backend"}

# Placeholder endpoints (to be expanded)
@app.get("/items")
async def get_items():
    return {"items": [{"id": 1, "name": "Item 1", "quantity": 10}]}

@app.post("/add-item")
async def add_item(name: str, qty: int):
    return {"message": f"Added {name} with quantity {qty}"}