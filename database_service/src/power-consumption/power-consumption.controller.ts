import { Controller } from '@nestjs/common';
import { GrpcMethod, MessagePattern, Payload } from '@nestjs/microservices';
import { PowerConsumptionService } from './power-consumption.service';
import { CreatePowerConsumptionDto } from './dto/create-power-consumption.dto';
import { UpdatePowerConsumptionDto } from './dto/update-power-consumption.dto';

@Controller()
export class PowerConsumptionController {
  constructor(private readonly powerConsumptionService: PowerConsumptionService) {}

  @GrpcMethod('createPowerConsumption')
  create(@Payload() createPowerConsumptionDto: CreatePowerConsumptionDto) {
    return this.powerConsumptionService.create(createPowerConsumptionDto);
  }

  @MessagePattern('findAllPowerConsumption')
  findAll() {
    return this.powerConsumptionService.findAll();
  }

  @MessagePattern('findOnePowerConsumption')
  findOne(@Payload() id: number) {
    return this.powerConsumptionService.findOne(id);
  }

  @MessagePattern('updatePowerConsumption')
  update(@Payload() updatePowerConsumptionDto: UpdatePowerConsumptionDto) {
    return this.powerConsumptionService.update(updatePowerConsumptionDto.id, updatePowerConsumptionDto);
  }

  @MessagePattern('removePowerConsumption')
  remove(@Payload() id: number) {
    return this.powerConsumptionService.remove(id);
  }
}
