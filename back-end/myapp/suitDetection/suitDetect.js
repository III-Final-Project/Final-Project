const path = require('path');
require('dotenv').config({ path: path.join(__dirname, '../.env') });
// Imports the Google Cloud client library
const vision = require('@google-cloud/vision');
// const fs = require('fs');
const fetch = require('node-fetch');

// Set up Google Vision API url endpoint
let url = 'https://vision.googleapis.com/v1/images:annotate';
const key = process.env.GOOGLE_VISION_API_KEY;
url = `${url}?key=${key}`;

// SuitDetectionByHand By Handmake
// const image = fs.readFileSync('./resources/download.jpeg', { encoding: 'base64' });
function suitDetectionByHand(imgBase64) {
  const request = {
    requests: {
      features: [{ maxResults: 100, type: 'OBJECT_LOCALIZATION' }, { maxResults: 50, type: 'LABEL_DETECTION' }],
      image: { content: imgBase64 },
    },
  };
  // console.log(JSON.stringify(request));
  return fetch(url, {
    body: JSON.stringify(request),
    method: 'POST',
    headers: {
      'content-type': 'application/json; charset=UTF-8',
    },
  }).then((response) => response.json());
}

// By Google SDK
async function suitDetectionByGoogleSDK(fileName) {
  console.log(fileName);
  // const image = fs.readFileSync(fileName);
  // Creates a client
  const client = new vision.ImageAnnotatorClient();
  const request = {
    // requests: {
    //   features: [{ maxResults: 50, type: 'OBJECT_LOCALIZATION' }],
    //   image: { content: imgBase64 },
    // },
  };
  // Performs label detection on the image file
  const objectResults = await client.objectLocalization(request);
  //   const labelResults = await client.labelDetection(request);
  //   const labels = result.labelAnnotations;
  //   const faces = results[0].faceAnnotations;
  //   const label = labelResults[0];
  //   console.log(label);
  const object = objectResults[0].localizedObjectAnnotations;
  console.log(object);
  //   label.forEach((item) => console.log(item));
  //   object.forEach((item) => console.log(item));
// Return format
//   {
//   mid: '/m/03gx245',
//   languageCode: '',
//   name: 'Top',
//   score: 0.8575218915939331,
//   boundingPoly: {
//     vertices: [],
//     normalizedVertices: [ [Object], [Object], [Object], [Object] ]
//   }
// }
// {
//   mid: '/m/01llx7',
//   languageCode: '',
//   name: 'Bracelet',
//   score: 0.7167083024978638,
//   boundingPoly: {
//     vertices: [],
//     normalizedVertices: [ [Object], [Object], [Object], [Object] ]
//   }
// }
}
// suitDetectionByGoogleSDK('./resources/download.jpeg');
// suitDetectionByHand(image)
//   .then((data) => {
//     data.responses.forEach((element) => {
//       console.log(element);
//     });
//     // console.log(data);
//   }) // JSON from `response.json()` call
//   .catch((error) => { console.error(error); return error; });
module.exports = { suitDetectionByHand, suitDetectionByGoogleSDK };
