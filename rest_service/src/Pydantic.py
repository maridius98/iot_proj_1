from pydantic import BaseModel

class PowerConsumptionReply(BaseModel):
    id: str
    global_active_power: float
    global_reactive_power: float
    voltage: float
    global_intensity: float
    timestamp: int


class Reply(BaseModel):
    message: str

