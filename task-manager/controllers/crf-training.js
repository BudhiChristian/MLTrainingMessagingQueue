var environment = require('../environments/environment');
var { MQConnection } = require('../services/messaging.service')

var scheduleTraining = async (req, res) => {
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

module.exports = { scheduleTraining }