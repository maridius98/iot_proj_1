import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { Document } from 'mongoose';

@Schema()
export class PowerConsumptionDoc extends Document {
    @Prop()
    global_active_power: number;

    @Prop()
    global_reactive_power: number;

    @Prop()
    voltage: number;

    @Prop()
    global_intensity: number;

    @Prop()
    timestamp: number;
}

export const PowerConsumptionSchema = SchemaFactory.createForClass(PowerConsumptionDoc);
