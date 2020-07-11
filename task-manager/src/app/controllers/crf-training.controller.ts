
import { environment } from "../../environments/environment";
import { MQConnection } from "../../../dist/app/services/messaging.service";


export const scheduleTraining = async (req, res) => {
    try {
        let message = await MQConnection.publishDirectlyToQueue(
            environment.messagingConfigurations.crfTrainingQueue, 
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