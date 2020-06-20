var environment = require('../../environments/environment');

var multer = require('multer');
var router = require('express').Router();
var publishToQueue = require('../../services/messaging.service').publishToQueue

var upload = multer()
router.post('/', upload.single('file'), async (req, res, next) => {
    try {
        let message = await publishToQueue(environment.crfTrainingQueue, req.file.buffer)
        res.status(200).send({
            message: message
        });
    } catch (err) {
        console.log(err)
        res.status(500).send({
            message: err.message
        });
    }
});

module.exports = router