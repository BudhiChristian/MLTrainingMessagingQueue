var environment = require('./environments/environment')

var express = require('express');
var app = express();

const host = environment.runConfigurations.host;
const port = environment.runConfigurations.port;

app.use('/crf-ner', require('./models/crf-training'));

app.listen(port, host, () => {
    console.log(`Project Running on port ${port}`)
})