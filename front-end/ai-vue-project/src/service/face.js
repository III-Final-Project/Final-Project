import axios from 'axios';

const faceRequest = axios.create({
  baseURL: 'http://localhost:5000/',
  timeout: 1000,
});
const queryuserInfo = (data) => faceRequest.post('/userinfo', data);
const imgUpload = (data) => faceRequest.post('/img_upload', data);
const faceDetect = (data) => faceRequest.post('/face', data);

export default {
  imgUpload,
  queryuserInfo,
  faceDetect,
};
