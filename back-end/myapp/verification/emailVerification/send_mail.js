const nodemailer = require('nodemailer');
const path = require('path');
require('dotenv').config({ path: path.join(__dirname, '../../.env') });

const emailUser = process.env.GOOGLE_EMAIL_USER;
const emailPass = process.env.GOOGLE_EMAIL_PASS;

// Mailtrap version -> For Demo Purpose
// const transporter = nodemailer.createTransport({
//   host: 'smtp.mailtrap.io',
//   port: 2525,
//   auth: {
//     user: emailUser,
//     pass: emailPass,
//   },
// });

// const receiverTest = 'jeff14994@gmail.com';
const subject = '[From @x0mg\'s lovely warning] Please reset your password';
const text = 'Please follow the following instruction to reset your password';

function wrappedSendEmail(mailOptions) {
  return new Promise((resolve) => {
  // Google SMTP version -> For reality Purpose
    const transporter = nodemailer.createTransport({
      host: 'smtp.gmail.com',
      auth: {
        type: 'login', // default
        user: emailUser,
        pass: emailPass,
      },
    });
    // TODO: How do I get the return value from async fucntion?
    transporter.sendMail(mailOptions, (error, info) => {
      if (error) {
        console.log(error);
        console.log('\x1b[31m', '[INFO] Email Failed');
        resolve(false);
        return;
      }
      console.log('\x1b[32m', `[INFO] Email sent: ${info.response}`);
      resolve(true);
    });
  });
}
async function sendEmail(receiver) {
  const mailOptions = {
    from: emailUser,
    to: receiver,
    subject,
    text,
  };
  const resp = wrappedSendEmail(mailOptions);
  return resp;
}
// Testing
// sendEmail('123').then(
//   (status) => {
//     if (status) {
//       console.log('hihi');
//     } else {
//       console.log('nono');
//     }
//   },
// );

module.exports = sendEmail;
