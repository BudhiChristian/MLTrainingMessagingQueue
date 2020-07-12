import { environment } from "../../environments/environment";
import amqp, { Connection, Channel } from 'amqplib';

export class MQConnection {
    private static __connection: Connection;
    private static __channel: Channel;

    private static readonly __connectionUrl: string = environment.messagingConfigurations.messagingUrl;

    static async getChannel(): Promise<Channel> {
        if (!MQConnection.__channel) {
            console.log("connecting to rabbitmq");
            console.log(MQConnection.__connectionUrl);
            try {
                MQConnection.__connection = await amqp.connect(MQConnection.__connectionUrl);
                MQConnection.__channel = await MQConnection.__connection.createChannel();
                console.log("rabbitmq channel established");
            } catch (err) {
                console.error(err.message);
                MQConnection.close();
                console.error("rabbitmq collection failed");
            }
        }
        return MQConnection.__channel
    }

    static async publishDirectlyToQueue(queueName: string, data: Buffer): Promise<string> {
        let channel: Channel = await MQConnection.getChannel();
        if (!channel) {
            return "rabbitmq connection not established. try again.";
        }

        await channel.assertQueue(queueName, {
            durable: true
        });

        channel.sendToQueue(queueName, data, {
            persistent: true
        });

        return "successfully queued"
    }

    static close() {
        if (MQConnection.__channel) {
            MQConnection.__channel.close()
            MQConnection.__channel = null;
        }
        if (MQConnection.__connection) {
            MQConnection.__connection.close()
            MQConnection.__connection = null
        }
    }
}
// MQConnection.__channel = null;
// MQConnection.__connection = null;

process.on('exit', (code) => {
    MQConnection.close()
    console.log("rabbitmq channel closing")
})