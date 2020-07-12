import { Router } from 'express';
import multer from 'multer';

const router = Router();
const upload = multer()

import { CRFTrainingController } from '../controllers/crf-training.controller';

router.post('/train', upload.single('file'), CRFTrainingController.scheduleTraining)

module.exports = router