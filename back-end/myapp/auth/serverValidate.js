const pythonUser = process.env.PYTHON_USER;
const pythonPass = process.env.PYTHON_PASS;

module.exports = {
  verifyServerRequest: (body) => {
    const pythonUserName = body.userName;
    const pythonUserPassword = body.userPassword;
    // Verify Username and Userpassword from Python Server
    const rightUser = pythonUserName === pythonUser;
    const rightPass = pythonUserPassword === pythonPass;
    if (rightUser && rightPass) {
      return true;
    }
    return false;
  },
};
