var express = require('express');
var app = express();

const port = 3000;
const host = '0.0.0.0';

app.use('/crf-ner', require('./models/crf-training'));

app.listen(port, host, () => {
    console.log(`Project Running on port ${port}`)
})