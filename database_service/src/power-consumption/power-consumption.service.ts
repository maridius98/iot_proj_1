import { Injectable } from '@nestjs/common';
import { CreatePowerConsumptionDto } from './dto/create-power-consumption.dto';
import { UpdatePowerConsumptionDto } from './dto/update-power-consumption.dto';

@Injectable()
export class PowerConsumptionService {
  create(createPowerConsumptionDto: CreatePowerConsumptionDto) {
    return 'This action adds a new powerConsumption';
  }

  findAll() {
    return `This action returns all powerConsumption`;
  }

  findOne(id: number) {
    return `This action returns a #${id} powerConsumption`;
  }

  update(id: number, updatePowerConsumptionDto: UpdatePowerConsumptionDto) {
    return `This action updates a #${id} powerConsumption`;
  }

  remove(id: number) {
    return `This action removes a #${id} powerConsumption`;
  }
}
