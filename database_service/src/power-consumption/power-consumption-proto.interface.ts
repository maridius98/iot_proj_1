export interface PowerConsumption {
    id?: string;
    global_active_power: number;
    global_reactive_power: number;
    voltage: number;
    global_intensity: number;
    timestamp: number;
}
  
export interface Reply {
    message: string;
}

export interface TimestampRange {
    start_timestamp: number;
    end_timestamp: number;
}

export interface PowerConsumptionId {
    id: string;
}