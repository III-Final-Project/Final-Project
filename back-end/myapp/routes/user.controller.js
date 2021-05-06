const sendMail = require('../verification/mailVerfication/send_sms');
const sendEmail = require('../verification/emailVerification/send_mail');

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
};
