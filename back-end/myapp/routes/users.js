const express = require('express');
// import mysql configuration in variable pool
const pool = require('../config/database');

const router = express.Router();
// Create new user
const create = (data, res) => {
  // use mysql query to insert into data
  // console.log(data);
  pool.query(
    'insert into User (user_id, user_name, user_email, user_address, user_mobile, user_password, pass_desc, pass_type, login_time, login_ip, create_time, role_id)'
    + ' values (?,?,?,?,?,?,?,?,?,?,?,?)',
    [
      data.body.user_id,
      data.body.user_name,
      data.body.user_email,
      data.body.user_address,
      data.body.user_mobile,
      data.body.user_password,
      data.body.pass_desc,
      data.body.pass_type,
      data.body.login_time,
      data.body.login_ip,
      data.body.create_time,
      data.body.role_id,
    ],
    // callback function of pool.query has three parameters
    (error) => {
      if (error) {
        // callBack(error);
        // console.log(error.sqlMessage);
        // console.log(error.sql);
        res.json({
          returnCode: '500',
          detail: 'error',
        });
      } else {
      // return callBack(null, results);
      // res.json(results);
      // console.log(results);
        res.status(200).json({
          returnCode: '200',
          detail: 'success',
        });
      }
    },
  );
};
// Retrieve all users
const getAllUser = (req, res) => {
  const response = {};
  console.log(req);
  pool.query(
    // 'select * from user where user_id = 1',
    'select user_id, user_name,  user_email, user_address, user_mobile, role_name, pass_type, create_time, login_time, login_ip from User '
    + ' INNER JOIN  Roles ON `User`.role_id = Roles.role_id',
    (error, results) => {
      if (error) {
        // callBack(error);
        console.log(error);
      }
      // callBack is a callback function from req, res and results[0] means get part of response
      // return callBack(null, results[0]);
      console.log(results);
      response.returnCode = '200';
      response.detail = results;
      res.json(response);
    },
  );
};
// Retrieve single user by ID
const getUserByID = (req, res) => {
  console.log(req.params.id);
  pool.query(
    'select user_id, user_name,  user_email, user_address, user_mobile, role_name, pass_type, create_time, login_time, login_ip from User'
    + ' INNER JOIN  Roles ON User.role_id = Roles.role_id where user_id = ?',
    [req.params.id],
    (error, results) => {
      if (error) {
        res.json({
          returnCode: '500',
          detail: 'error',
        });
      }
      if (!results) {
        res.json({
          returnCode: '200',
          detail: results,
        });
      }
      res.json({
        returnCode: '200',
        detail: 'empty',
      });
    },
  );
};
// Update
const modifyUserInfo = (req, res) => {
  // console.log(req.body);
  pool.query(
    'update User set user_name=?,  user_email=?, user_address=?, user_mobile=?, user_password=?, pass_desc=?, pass_type=?, login_time=?, login_ip=?, create_time=?, role_id=? where user_id = ?',
    [
      req.body.user_name,
      req.body.user_email,
      req.body.user_address,
      req.body.user_mobile,
      req.body.user_password,
      req.body.pass_desc,
      req.body.pass_type,
      req.body.login_time,
      req.body.login_ip,
      req.body.create_time,
      req.body.role_id,
      req.body.user_id,
    ],
    (error) => {
      if (error) {
        res.json({
          returnCode: '500',
          detail: 'error',
        });
      } else {
        res.json({
          returnCode: '200',
          detail: 'success',
        });
      }
    },
  );
};
// Delete
const deleteUser = (req, res) => {
  pool.query(
    'delete from User where user_id = ?',
    [req.body.user_id],
    (error) => {
      if (error) {
        res.json({
          returnCode: '500',
          detail: 'error',
        });
      } else {
        res.json({
          returnCode: '200',
          detail: 'success',
        });
      }
    },
  );
};
router.get('/', getAllUser);
router.get('/:id', getUserByID);
router.post('/', create);
router.patch('/', modifyUserInfo);
router.delete('/', deleteUser);

module.exports = router;
