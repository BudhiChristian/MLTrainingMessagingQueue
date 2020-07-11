var router = require('express').Router();
var multer = require('multer')
var upload = multer()

import { scheduleTraining } from '../controllers/crf-training.controller';

router.post('/train', upload.single('file'), scheduleTraining)

module.exports = router