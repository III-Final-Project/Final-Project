const chaiHttp = require('chai-http');

const chai = require('../node_modules/chai');
const app = require('../app');

chai.should();
chai.use(chaiHttp);

describe('', () => {
  it('It should GET all the users', (done) => {
    chai.request(app)
      .get('/users')
      .end((err, res) => {
        res.should.have.status(200);
        res.body.should.be.a('object');
        res.body.should.have.property('returnCode').eql('200');
        res.body.detail.should.be.a('array');
        done();
      });
  });
});
