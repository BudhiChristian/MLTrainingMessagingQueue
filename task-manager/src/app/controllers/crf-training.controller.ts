
import { environment } from "../../environments/environment";
import { MQConnection } from "../../../dist/app/services/messaging.service";
import { Response, Request } from "express";
import { ExecutionTimeLogger } from "../services/logging.service";

export class CRFTrainingController {
    private static readonly queueName: string = environment.messagingConfigurations.crfTrainingQueue;

    @ExecutionTimeLogger()
    static async scheduleTraining(req: Request, res: Response): Promise<void> {
        try {
            let message = await MQConnection.publishDirectlyToQueue(
                CRFTrainingController.queueName, 
                req.file.buffer
            )
            res.status(200).send({
                message: message
            });
        } catch (err) {
            console.error(err)
            res.status(500).send({
                message: err.message
            });
        }
    }
}