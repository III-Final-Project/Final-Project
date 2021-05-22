import axios from 'axios';

const userRequest = axios.create({
  baseURL: 'http://localhost:4000/users',
  timeout: 1000,
});
// const queryUsers = userRequest.get('/');
const queryUsersById = (id) => userRequest.get(`/${id}`);
const createUsers = (data) => userRequest.post('/', data);
const updatedUser = (data) => userRequest.put('/', data);
const deleteUser = (data) => userRequest.delete('/', data);
const userSMS = (data) => userRequest.post('/sms', data);

export default {
  // queryUsers,
  queryUsersById,
  createUsers,
  updatedUser,
  deleteUser,
  userSMS,
};
