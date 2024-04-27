from fastapi import FastAPI
from grpc import insecure_channel
from google.protobuf.timestamp_pb2 import Timestamp
from src.Pydantic import PowerConsumptionReply, Reply
from src.PowerConsumption_pb2 import PowerConsumption, PowerConsumptionId
from src.PowerConsumption_pb2_grpc import PowerConsumptionServiceStub

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    global channel
    channel = insecure_channel('server:50051')

@app.on_event("shutdown")
async def shutdown_event():
    global channel
    channel.close()

@app.get("/")
async def get(id: str) -> PowerConsumptionReply:
    stub = PowerConsumptionServiceStub(channel)
    power_consumption_id = PowerConsumptionId(id=id)
    response = await stub.Read(power_consumption_id)
    return response

@app.post("/")
async def post(power_consumption: PowerConsumptionReply) -> Reply:
    stub = PowerConsumptionServiceStub(channel)
    response = await stub.Create(power_consumption)
    return response