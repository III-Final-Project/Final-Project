const express = require('express');

const router = express.Router();

/* GET home page. */
router.get('/', (req, res) => {
  res.render('index', { title: '0M9, WH0m 4M1 , wH3r3 4m1 1, WhY M 1 h3R3 ???' });
});

module.exports = router;
