const jwt = require('jsonwebtoken');

const key = process.env.JWT_KEY;
module.exports = {
  // eslint-disable-next-line consistent-return
  verifyToken: (req, res, next) => {
    let token = req.get('authorization');
    if (!token) {
      return res.status(400).json({
        returnCode: '400',
        detail: 'Bring JWT in authorization in Header',
      });
    }
    token = token.slice(7);
    // If token exists
    if (token) {
      // eslint-disable-next-line consistent-return
      jwt.verify(token, key, (error, decoded) => {
        if (error) {
          return res.status(403).json({
            returnCode: '403',
            detail: 'Invalid Token',
          });
        }
        req.deocded = decoded;
        next();
      });
    }
  },
};
