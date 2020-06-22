const environment = {
    runConfigurations: {
        host: '0.0.0.0',
        port: 3000
    },
    messagingConfigurations: {
        messagingUrl: "amqp://0.0.0.0",
        crfTrainingQueue: "crf_training_queue"
    }
};

module.exports = environment;