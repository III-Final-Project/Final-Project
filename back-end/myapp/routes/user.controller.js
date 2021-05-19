// import json web token
const { sign } = require('jsonwebtoken');

const { hashSync, genSaltSync, compareSync } = require('bcrypt');
const sendMail = require('../verification/mailVerfication/send_sms');
const sendEmail = require('../verification/emailVerification/send_mail');
const { create, getUserByNamePost } = require('./user.service');
const { suitDetectionByHand } = require('../suitDetection/suitDetect');

module.exports = {
  // Verify telephones
  verificationCode: (req, res) => {
    const { telephone } = req.body;
    const code = sendMail(telephone);
    const returnFormat = {};
    // TODO: Remember to conduct error handling
    returnFormat.returnCode = '200';
    returnFormat.detail = `${code}`;
    // console.log('testing');
    console.log(`The user's verification Code is: ${code}`);
    res.send(returnFormat);
    // res.send('omg');
  },

  resetPassword: (req, res) => {
    const { email } = req.body;
    // const msg = sendEmail(email);
    sendEmail(email).then(
      (status) => {
        const returnFormat = {};
        if (status) {
          returnFormat.returnCode = '200';
          returnFormat.detail = 'Email sent';
          res.send(returnFormat);
          return;
        }
        returnFormat.returnCode = '500';
        returnFormat.detail = 'Sending failed';
        res.send(returnFormat);
      },
    );
  },
  createUser: (req, res) => {
    // encrypt the password with salt and hash
    const salt = genSaltSync(10);
    req.body.user_password = hashSync(req.body.user_password, salt);
    create(req, res);
  },
  login: (req, res) => {
    const { body } = req;
    getUserByNamePost(body.user_name, (err, results) => {
      // MySQL Error handling
      if (err) {
        console.log(`Error message: ${err}`);
        return res.status(500).json({
          returnCode: '500',
          detail: err.code,
        });
      }
      // Wrong user name
      if (!results) {
        return res.json({
          returnCode: '200',
          detail: 'Invalid username',
        });
      }
      // Compare user input password with database password
      const result = compareSync(body.user_password, results.user_password);
      if (result) {
        // sign consumes three parameters: object(password), key, object(expires time)
        const key = process.env.JWT_KEY;
        const jsontoken = sign({ result: results }, key, {
          expiresIn: '1h',
        });
        return res.status(200).json({
          returnCode: '200',
          detail: 'login successfully',
          token: jsontoken,
        });
      }
      // Wrong  password
      return res.status(500).json({
        returnCode: '500',
        detail: 'Invalid username or password',
      });
    });
  },
  suitDetect: (req, res) => {
    // console.log(req.body.image);
    suitDetectionByHand(req.body.image)
      .then((data) => {
        const response = {
          returnCode: '200',
          detail: data.responses,
        };
        // console.log(data);
        // Correct responses
        if (data.responses) {
          res.status(200).json(response);
          return;
        }
        // Error responses
        res.status(400).json({
          returnCode: '400',
          detail: data.error.message,
        });
        // console.log(data);
      }) // JSON from `response.json()` call
      .catch((error) => { console.error(error); res.send(error); });
  },
};
