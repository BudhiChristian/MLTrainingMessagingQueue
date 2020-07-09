var router = require('express').Router();
var multer = require('multer')
var upload = multer()

var { scheduleTraining } = require('../controllers/crf-training')

router.post('/train', upload.single('file'), scheduleTraining)

module.exports = router