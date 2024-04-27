import { Injectable } from '@nestjs/common';
import { CreatePowerConsumptionDto } from './dto/create-power-consumption.dto';
import { UpdatePowerConsumptionDto } from './dto/update-power-consumption.dto';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { PowerConsumptionDoc } from './entities/power-consumption.schema';
import { PowerConsumption, Reply } from './power-consumption-proto.interface';

@Injectable()
export class PowerConsumptionService {
  constructor(@InjectModel('PowerConsumption') private model: Model<PowerConsumptionDoc>) {}

  async create(dto: PowerConsumption): Promise<Reply> {
    await this.model.create(dto);
    return {message: "Success"};
  }

  async findOne(id: string): Promise<PowerConsumption> {
    const doc = await this.model.findById(id);
    return this.docToInterface(doc);
  }

  async update(dto: PowerConsumption): Promise<Reply> {
    const {id, ...rest} = dto
    await this.model.findByIdAndUpdate(id, rest);
    return {message: "Success"};
  }

  async remove(id: string): Promise<Reply> {
    await this.model.findByIdAndDelete(id);
    return {message: "Success"};
  }

  private docToInterface(doc: PowerConsumptionDoc): PowerConsumption {
    return {
      id: doc.id,
      global_active_power: doc.global_active_power,
      global_reactive_power: doc.global_reactive_power,
      global_intensity: doc.global_intensity,
      timestamp: doc.timestamp,
      voltage: doc.voltage
    }
  }
}
