const path = require('path');
require('dotenv').config({ path: path.join(__dirname, '../../.env') });
// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
// and set the environment variables. See http://twil.io/secure
// TWILIO_ACCOUNT_SID=AC80833c116b16ec0fc811dbfd6ca70468
// TWILIO_AUTH_TOKEN=78a8f397546a489f93cab39a312f5e8c
const accountSid = process.env.TWILIO_ACCOUNT_SID;
const authToken = process.env.TWILIO_AUTH_TOKEN;
// const tellphoneNumber = '0911867605';

// Import twilio module
const client = require('twilio')(accountSid, authToken);

// Sent message from twilio
const sendVerificationCode = (tellInput) => {
  // Adjust the tellphone input
  // Filter tellphone number to 0911867605 to +886911867605
  const tell = `+886${tellInput.substring(1)}`;
  // console.log(tell);
  // Randomly generate verification code
  const randNum = Math.floor(1000 + Math.random() * 9000);
  client.messages
    .create({
      body: `Hello Customer, your verification code is ${randNum}`,
      from: '+18084685402',
      //   from: '+14159806318',
      // to: '+886911867605',
      to: tell,
    })
    .then((message) => console.log(`Mail Sent: ${message.dateCreated}`));
  return randNum;
};

// console.log(randNum);
// sendVerificationCode(tellphoneNumber);
module.exports = sendVerificationCode;
