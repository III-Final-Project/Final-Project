import axios from 'axios';

const faceRequest = axios.create({
  baseURL: 'http://localhost:5000/',
  timeout: 1000,
});
const imgUpload = (data) => faceRequest.post('/img_upload', data);

export default {
  imgUpload,
};
