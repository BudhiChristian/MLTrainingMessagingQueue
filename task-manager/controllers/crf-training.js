var environment = require('../environments/environment');
var { publishToQueue } = require('../services/messaging.service')

var scheduleTraining = async (req, res) => {
    try {
        let message = await publishToQueue(
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