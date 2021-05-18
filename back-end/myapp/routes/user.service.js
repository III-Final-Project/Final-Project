// import mysql configuration in variable pool
const pool = require('../config/database');

module.exports = {
// Create new user
  create: (data, res) => {
    // use mysql query to insert into data
    const passDesc = 'I am a new user';
    const passType = 'basic permission';
    const createTime = new Date().toISOString().slice(0, 19).replace('T', ' ');
    // TODO: Update login time when Login
    const loginTime = createTime;
    const ipAddress = data.ip.substring(7);
    const roleId = '3';
    // console.log(createTime);
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
        passDesc,
        passType,
        loginTime,
        ipAddress,
        createTime,
        roleId,
      ],
      // callback function of pool.query has three parameters
      (error) => {
        if (error) {
          // callBack(error);
          // console.log(error.sqlMessage);
          // console.log(error.sql);
          res.status(500).json({
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
  },
  // Retrieve all users
  getAllUser: (req, res) => {
    const response = {};
    // console.log(req);
    pool.query(
      // 'select * from user where user_id = 1',
      'select user_id, user_name,  user_email, user_address, user_mobile, role_name, pass_type, create_time, login_time, login_ip from User '
      + ' INNER JOIN  Roles ON `User`.role_id = Roles.role_id',
      (error, results) => {
        if (error) {
          // callBack(error);
          // console.log(error);
          res.status(500).json({
            returnCode: '500',
            detail: 'error',
          });
        }
        // callBack is a callback function from req, res and results[0] means get part of response
        // return callBack(null, results[0]);
        // console.log(results);
        response.returnCode = '200';
        response.detail = results;
        res.json(response);
      },
    );
  },
  // Retrieve single user by ID
  getUserByID: (req, res) => {
    // console.log(req.params.id);
    pool.query(
      'select user_id, user_name,  user_email, user_address, user_mobile, role_name, pass_type, create_time, login_time, login_ip from User'
      + ' INNER JOIN  Roles ON User.role_id = Roles.role_id where user_id = ?',
      [req.params.id],
      (error, results) => {
        if (error) {
          res.status(500).json({
            returnCode: '500',
            detail: 'error',
          });
          return;
        }
        // console.log(results);
        // Check if user exists in database
        if (results.length !== 0) {
          res.json({
            returnCode: '200',
            detail: results,
          });
        // Return empty when user not exist
        } else {
          res.json({
            returnCode: '200',
            detail: 'empty',
          });
        }
      },
    );
  },
  getUserByName: (req, res) => {
    // console.log(req.params.username);
    pool.query(
      'select user_id, user_name, user_email, user_address, user_mobile, role_name, pass_type, create_time, login_time, login_ip from User'
      + ' INNER JOIN  Roles ON User.role_id = Roles.role_id where user_name = ?',
      [req.params.username],
      (error, results) => {
        // console.log(req.params.username);
        if (error) {
          res.status(500).json({
            returnCode: '500',
            detail: 'error',
          });
          return;
        }
        // Check if user exists in database
        if (results.length !== 0) {
          res.json({
            returnCode: '200',
            detail: results,
          });
        // Return empty when user not exist
        } else {
          res.json({
            returnCode: '200',
            detail: 'empty',
          });
        }
      },
    );
  },
  getUserByNamePost: (userName, callback) => {
    // console.log(req.body.user_name);
    pool.query(
      'select * from User'
      + ' INNER JOIN  Roles ON User.role_id = Roles.role_id where user_name = ?',
      [userName],
      (error, results) => {
        if (error) {
          callback(error);
        }
        // null means callback's first parameter error is empty
        // results[0] means obtain the first element from the object
        console.log(results);
        return callback(null, results[0]);
      },
    );
  },
  // Update
  modifyUserInfo: (req, res) => {
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
          res.status(500).json({
            returnCode: '500',
            detail: 'error',
            // msg: error,
          });
        } else {
          res.json({
            returnCode: '200',
            detail: 'success',
          });
        }
      },
    );
  },
  // Delete
  deleteUser: (req, res) => {
    pool.query(
      'delete from User where user_id = ?',
      [req.body.user_id],
      (error) => {
        if (error) {
          res.status(500).json({
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
  },
};
