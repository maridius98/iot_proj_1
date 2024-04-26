import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { PowerConsumptionModule } from './power-consumption/power-consumption.module';

@Module({
  imports: [PowerConsumptionModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
