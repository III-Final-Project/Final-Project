const express = require('express');
// import mysql configuration in variable pool
const pool = require('../config/database');

const router = express.Router();
const getUserByUserEmail = (req, res) => {
  const response = {};
  pool.query(
    // 'select * from user where user_id = 1',
    'select user_id, user_name,  user_email, user_address, user_mobile, role_name, pass_type, create_time, login_time, login_ip from user'
    + ' INNER JOIN Create_status on `User`.create_id = Create_status.create_id'
    + ' INNER JOIN  Roles ON `User`.role_id = Roles.role_id'
    + ' INNER JOIN Passwords ON `User`.pass_id = Passwords.pass_id'
    + ' INNER JOIN Login ON user.login_id = Login.login_id LIMIT 0, 2',
    // [id],
    (error, results) => {
      if (error) {
        // callBack(error);
        console.log(error);
      }
      // callBack is a callback function from req, res and results[0] means get part of response
      // return callBack(null, results[0]);
      console.log(results);
      response.returnCode = '200';
      response.data = results;
      res.json(response);
    },
  );
};
/* GET users listing. */
// router.get('/', (req, res) => {
//   res.send('respond with a resource');
// });
router.get('/', getUserByUserEmail);

module.exports = router;
