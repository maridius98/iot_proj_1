import { Controller } from '@nestjs/common';
import { GrpcMethod, MessagePattern, Payload } from '@nestjs/microservices';
import { PowerConsumptionService } from './power-consumption.service';
import { Metadata, ServerUnaryCall } from '@grpc/grpc-js';
import { PowerConsumptionId, PowerConsumption, Reply, TimestampRange} from './power-consumption-proto.interface';

@Controller()
export class PowerConsumptionController {
  constructor(private readonly powerConsumptionService: PowerConsumptionService) {}

  @GrpcMethod('PowerConsumptionService', 'Create')
  async create(data: PowerConsumption, metadata: Metadata, call: ServerUnaryCall<any, any>) {
    console.log(JSON.stringify(data))
    return await this.powerConsumptionService.create(data);
  }

  @GrpcMethod('PowerConsumptionService')
  async read(data: PowerConsumptionId) {
    return await this.powerConsumptionService.findOne(data.id);
  }

  @GrpcMethod('PowerConsumptionService')
  async update(data: PowerConsumption) {
    return await this.powerConsumptionService.update(data);
  }

  @GrpcMethod('PowerConsumptionService')
  async remove(data: PowerConsumptionId) {
    return await this.powerConsumptionService.remove(data.id);
  }
}
