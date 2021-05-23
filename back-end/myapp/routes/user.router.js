const router = require('express').Router();

// Member service
const {
  getAllUser, getUserByID, getUserByName, modifyUserInfo, deleteUser,
} = require('./user.service');
// Core service
const {
  login, createUser, verificationCode, resetPassword, suitDetect,
} = require('./user.controller');
// JWT validataion
const { verifyToken } = require('../auth/tokenValidate');

// With JWT validation
router.get('/', verifyToken, getAllUser);
router.get('/:id', verifyToken, getUserByID);
router.get('/queryname/:username', verifyToken, getUserByName);
router.post('/', createUser);
router.patch('/', verifyToken, modifyUserInfo);
router.delete('/', verifyToken, deleteUser);
router.post('/sms', verificationCode);
router.post('/email', resetPassword);
router.post('/login', login);
router.post('/suitdetect', suitDetect);

// Without JWT validation
// router.get('/', getAllUser);
// router.get('/:id', getUserByID);
// router.get('/queryname/:username', getUserByName);
// router.post('/', createUser);
// router.patch('/', modifyUserInfo);
// router.delete('/', deleteUser);
// router.post('/sms', verificationCode);
// router.post('/email', resetPassword);
// router.post('/login', login);
// router.post('/suitdetect', suitDetect);

module.exports = router;
