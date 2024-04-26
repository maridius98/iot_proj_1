import { PartialType } from '@nestjs/mapped-types';
import { CreatePowerConsumptionDto } from './create-power-consumption.dto';

export class UpdatePowerConsumptionDto extends PartialType(CreatePowerConsumptionDto) {
  id: number;
}
