import axios from 'axios';

const faceRequest = axios.create({
  baseURL: 'http://localhost:5000/',
  timeout: 1000,
});
const queryuserInfo = (data) => faceRequest.post('/api/user', data);
const imgUpload = (data) => faceRequest.post('/api/user/img_upload', data);
const faceDetect = (data) => faceRequest.post('/api/user/face', data);
export default {
  imgUpload,
  queryuserInfo,
  faceDetect,
};
