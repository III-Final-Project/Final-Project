const router = require('express').Router();

const {
  getAllUser, getUserByID, getUserByName, modifyUserInfo, deleteUser,
} = require('./user.service');
const {
  login, createUser, verificationCode, resetPassword,
} = require('./user.controller');

router.get('/', getAllUser);
router.get('/:id', getUserByID);
router.get('/queryname/:username', getUserByName);
router.post('/', createUser);
router.patch('/', modifyUserInfo);
router.delete('/', deleteUser);
router.post('/sms', verificationCode);
router.post('/email', resetPassword);
router.post('/login', login);

module.exports = router;
