var environment = require('../environments/environment')
var amqp = require('amqplib')

class MQConnection {
    static async getChannel() {
        if (!MQConnection.channel) {
            console.log("connecting to rabbitmq")
            console.log(environment.messagingConfigurations.messagingUrl)
            try {
                MQConnection.connection = await amqp.connect(environment.messagingConfigurations.messagingUrl)
                MQConnection.channel = await MQConnection.connection.createChannel();
                console.log("rabbitmq channel established")
            } catch (err) {
                console.error(err)
                MQConnection.close()
                console.error("rabbitmq collection failed")
            }
        }
        return MQConnection.channel
    }

    static close() {
        if (MQConnection.channel) {
            MQConnection.channel.close()
            MQConnection.channel = null;
        }
        if (MQConnection.connection) {
            MQConnection.connection.close()
            MQConnection.connection = null
        }
    }
}

process.on('exit', (code) => {
    MQConnection.close()
    console.log("rabbitmq channel closing")
})

const publishToQueue = async (queueName, data) => {
    let channel = await MQConnection.getChannel()
    if (!channel) {
        return "rabbitmq connection not establish. try again."
    }

    await channel.assertQueue(queueName, {
        durable: true
    })
    
    channel.sendToQueue(queueName, data, {
        persistent: true
    })
    return "successfully queued"
}

module.exports = { publishToQueue }