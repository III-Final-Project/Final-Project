const path = require('path');
require('dotenv').config({ path: path.join(__dirname, '../../.env') });
// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
// and set the environment variables. See http://twil.io/secure
const accountSid = process.env.TWILIO_ACCOUNT_SID;
const authToken = process.env.TWILIO_AUTH_TOKEN;

// Import twilio module
const client = require('twilio')(accountSid, authToken);

// Sent message from twilio
const sendVerificationCode = (tellInput) => {
  // Adjust the tellphone input
  // Filter tellphone number to 0912345678 to +886912345678
  const tell = `+886${tellInput.substring(1)}`;
  // console.log(tell);
  // Randomly generate verification code
  const randNum = Math.floor(1000 + Math.random() * 9000);
  client.messages
    .create({
      body: `Hello Customer, your verification code is ${randNum}`,
      from: '+18084685402',
      to: tell,
    })
    .then((message) => console.log(`Mail Sent: ${message.dateCreated}`));
  return randNum;
};

// console.log(randNum);
// sendVerificationCode(tellphoneNumber);
module.exports = sendVerificationCode;
