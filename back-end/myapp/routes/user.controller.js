const sendMail = require('../verification/mailVerfication/send_sms');

module.exports = {
  // Verify telephones
  verificationCode: (req, res) => {
    const phoneNumber = req.body.telephone;
    const code = sendMail(phoneNumber);
    const returnFormat = {};
    returnFormat.returnCode = '200';
    returnFormat.detail = `${code}`;
    // console.log('testing');
    console.log(`The user's verification Code is: ${code}`);
    res.send(returnFormat);
    // res.send('omg');
  },
};
