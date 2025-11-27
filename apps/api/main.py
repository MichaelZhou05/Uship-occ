# from fastapi import FastAPI
# from sqlmodel import SQLModel
# from database import Engine

# # 1. Initialize the App
# app = FastAPI(
#     title="Ushipp OCC API",
#     description="Operations Command Center Backend",
#     version="0.1.0"
# )

# # 2. Event: On Startup
# @app.on_event("startup")
# def on_startup():
#     # This creates the tables if they don't exist (useful for dev)
#     # In production, we usually use migration tools like Alembic
#     SQLModel.metadata.create_all(engine)

# # 3. Basic Route (The "Health Check")
# @app.get("/")
# def read_root():
#     return {
#         "status": "online", 
#         "service": "Ushipp Backend",
#         "environment": "development"
#     }

# # 4. Example Route: Ingest Webhook (Skeleton)
# @app.post("/api/v1/webhooks/wix-order")
# def ingest_order(payload: dict):
#     # This is where we will write the logic later
#     print(f"Received Order from Wix: {payload}")
#     return {"status": "received", "order_id": payload.get("id")}