from fastapi import FastAPI

app = FastAPI()

items = [
    {"name": "mango", "description": "a fruit"},
    {"name": "cabbage", "description": "a vegetable"},
    {"name": "beef", "description": "meat"}
]

@app.get("/api/items")
async def read_items():
    return items
