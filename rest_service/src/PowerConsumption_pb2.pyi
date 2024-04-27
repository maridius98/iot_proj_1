from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PowerConsumption(_message.Message):
    __slots__ = ("id", "global_active_power", "global_reactive_power", "voltage", "global_intensity", "timestamp")
    ID_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_ACTIVE_POWER_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_REACTIVE_POWER_FIELD_NUMBER: _ClassVar[int]
    VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_INTENSITY_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    id: str
    global_active_power: float
    global_reactive_power: float
    voltage: float
    global_intensity: float
    timestamp: int
    def __init__(self, id: _Optional[str] = ..., global_active_power: _Optional[float] = ..., global_reactive_power: _Optional[float] = ..., voltage: _Optional[float] = ..., global_intensity: _Optional[float] = ..., timestamp: _Optional[int] = ...) -> None: ...

class Reply(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class TimestampRange(_message.Message):
    __slots__ = ("start_timestamp", "end_timestamp")
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    start_timestamp: int
    end_timestamp: int
    def __init__(self, start_timestamp: _Optional[int] = ..., end_timestamp: _Optional[int] = ...) -> None: ...

class Value(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...

class PowerConsumptionId(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
