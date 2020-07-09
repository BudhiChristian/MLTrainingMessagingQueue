var environment = require('./environments/environment')

var express = require('express');
var app = express();

const host = environment.runConfigurations.host;
const port = environment.runConfigurations.port;

app.use('/crf-ner', require('./routes/crf-training'));

app.get('/env', (req, res) => {
    res.status(200).send(environment)
})

app.listen(port, host, () => {
    console.log(`Project Running on port ${port}`)
})