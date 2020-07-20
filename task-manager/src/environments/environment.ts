export const environment = {
    runConfigurations: {
        host: '0.0.0.0',
        port: 3000
    },
    messagingConfigurations: {
        messagingUrl: `amqp://${process.env.RABBITMQ_HOST || '0.0.0.0'}`,
        exchangeName: "training_exchange",
        crfTraining: {
            rolutingKey: "ner.crf"
        }
    }
};