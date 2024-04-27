import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';
import { PowerConsumptionService } from './power-consumption.service';
import { PowerConsumptionController } from './power-consumption.controller';
import { PowerConsumptionSchema } from './entities/power-consumption.schema';

@Module({
  imports: [
    MongooseModule.forRoot('mongodb://db:27017/test'),
    MongooseModule.forFeature([{ name: 'PowerConsumption', schema: PowerConsumptionSchema }])
  ],

  controllers: [PowerConsumptionController],
  providers: [PowerConsumptionService],
})
export class PowerConsumptionModule {}
