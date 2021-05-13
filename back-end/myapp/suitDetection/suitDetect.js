// Imports the Google Cloud client library
const vision = require('@google-cloud/vision');
const fs = require('fs');

async function quickstart(fileName) {
  console.log(fileName);
  const image = fs.readFileSync(fileName);
  // Creates a client
  const client = new vision.ImageAnnotatorClient();
  const request = {
    image: { content: image, features: [{ maxResults: 50 }] },
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
quickstart('./resources/download.jpeg');
