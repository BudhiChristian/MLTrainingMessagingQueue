import express from 'express';

import { environment } from './environments/environment'

const app = express();
const host = environment.runConfigurations.host;
const port = environment.runConfigurations.port;

app.use('/crf-ner', require('./app/routes/crf-training.route'));

app.get('/env', (req, res) => {
    res.status(200).send(environment)
})

app.listen(port, host, () => {
    console.log(`Project Running on port ${port}`)
})