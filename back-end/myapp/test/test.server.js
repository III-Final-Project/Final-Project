const chaiHttp = require('chai-http');

const chai = require('../node_modules/chai');
const app = require('../app');

chai.should();
chai.use(chaiHttp);

describe('Test Basic CRUD', () => {
  // Unit test GET method
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
  describe('', () => {
    it('It should GET only one specific user', (done) => {
      chai.request(app)
        .get('/users/1')
        .end((err, res) => {
          res.should.have.status(200);
          res.body.should.be.a('object');
          res.body.should.have.property('returnCode').eql('200');
          res.body.detail.should.be.a('array');
          done();
        });
    });
  });
  describe('', () => {
    it('It should not GET detail if user id is not existed', (done) => {
      chai.request(app)
        .get('/users/-1')
        .end((err, res) => {
          res.should.have.status(200);
          res.body.should.be.a('object');
          res.body.should.have.property('returnCode').eql('200');
          res.body.detail.should.be.a('string');
          done();
        });
    });
  });

  // Unit test POST method
  describe('', () => {
    it('It should POST a user', (done) => {
      const user = {
        user_name: 'I am a test',
        user_email: 'ggg@gmail.com',
        user_address: '@where',
        user_mobile: '0988767666',
        user_password: '123',
        // login_time: '2009-10-04 22:23:00',
        // login_ip: '192.167.1.1',
        // create_time: '2009-10-04 22:23:00',
        // role_id: '3',
      };
      chai.request(app)
        .post('/users')
        .send(user)
        .end((err, res) => {
          res.should.have.status(200);
          res.body.should.be.a('object');
          res.body.should.have.property('returnCode').eql('200');
          res.body.should.have.property('detail').eql('success');
          done();
        });
    });
  });

  describe('', () => {
    it('It should not POST a user', (done) => {
      const user = {
        user_name: 'I am a test',
        // user_email: 'ggg@gmail.com',
        user_address: '@where',
        user_mobile: '0988767666',
        user_password: '123',
        login_time: '2009-10-04 22:23:00',
        login_ip: '192.167.1.1',
        create_time: '2009-10-04 22:23:00',
        role_id: '3',
      };
      chai.request(app)
        .post('/users')
        .send(user)
        .end((err, res) => {
          res.should.have.status(500);
          res.body.should.be.a('object');
          res.body.should.have.property('returnCode').eql('500');
          res.body.should.have.property('detail').eql('error');
          done();
        });
    });
  });
  // Unit test PATCH method
  // Unit test DELETE method
});
