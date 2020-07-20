import { environment } from "../../environments/environment";
import amqp, { Connection, Channel } from 'amqplib';

export class MQConnection {
    private static __connection: Connection;
    private static __channel: Channel;

    private static readonly __connectionUrl: string = environment.messagingConfigurations.messagingUrl;
    private static readonly __exchangeName: string = environment.messagingConfigurations.exchangeName;

    static async getChannel(): Promise<Channel> {
        if (!MQConnection.__channel) {
            console.log("connecting to rabbitmq");
            console.log(MQConnection.__connectionUrl);
            try {
                // await and check again in case connection was created in a parallel thread
                let connection = await amqp.connect(MQConnection.__connectionUrl);
                if (!MQConnection.__connection) {
                    MQConnection.__connection = connection;
                } else {
                    connection.close();
                }
                
                let channel = await MQConnection.__connection.createChannel();
                if(!MQConnection.__channel) { 
                    MQConnection.__channel = channel;
                } else {
                    channel.close();
                    connection.close();
                }

                //Assert Exchange
                await MQConnection.__channel.assertExchange(MQConnection.__exchangeName, 'topic', {
                    durable: true
                })
                console.log("rabbitmq channel established");
            } catch (err) {
                console.error(err.message);
                MQConnection.close();
                console.error("rabbitmq collection failed");
            }
        }
        return MQConnection.__channel
    }

    static async publish(key: string, data: Buffer): Promise<string> {
        let channel: Channel = await MQConnection.getChannel();
        if (!channel) {
            return "rabbitmq connection not established. try again.";
        }

        channel.publish(MQConnection.__exchangeName, key, data);

        return "successfully queued"
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

process.on('exit', (code) => {
    MQConnection.close()
    console.log("rabbitmq channel closing")
})