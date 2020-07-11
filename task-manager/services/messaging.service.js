var environment = require('../environments/environment')
var amqp = require('amqplib')

class MQConnection {
    static async getChannel() {
        if (!MQConnection.__channel) {
            console.log("connecting to rabbitmq");
            console.log(environment.messagingConfigurations.messagingUrl);
            try {
                MQConnection.__connection = await amqp.connect(environment.messagingConfigurations.messagingUrl);
                MQConnection.__channel = await MQConnection.__connection.createChannel();
                console.log("rabbitmq channel established");
            } catch (err) {
                console.error(err);
                MQConnection.close();
                console.error("rabbitmq collection failed");
            }
        }
        return MQConnection.__channel
    }

    static async publishDirectlyToQueue(queueName, data) {
        let channel = await MQConnection.getChannel();
        if (!channel) {
            return "rabbitmq connection not establish. try again.";
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

module.exports = { MQConnection }