var router = require('express').Router();

router.use('/train', require('./queue-training'));

module.exports = router;