var environment = require('../environments/environment')
var amqp = require('amqplib/callback_api')

console.log("connecting to rabbitmq")
var channel = null;

amqp.connect(environment.messagingUrl, (err, connection) => {
    if(err) {
        throw err;
    }
    connection.createChannel((err, ch) => {
        if (err) {
            throw err;
        }
        channel = ch;
        console.log("rabbitmq channel established")
    })
});

process.on('exit', (code) => {
    channel.close();
    console.log("rabbitmq channel closing")
})

const publishToQueue = async (queueName, data) => {
    if (!channel) {
        return "rabbitmq connection not establish. try again."
    }

    channel.assertQueue(queueName, {
        durable: true
    })
    channel.sendToQueue(queueName, data, {
        persistent: true
    })
    return "successfully queued"
}

module.exports = { publishToQueue }