const chaiHttp = require('chai-http');

const chai = require('../node_modules/chai');
const app = require('../app');

chai.should();
chai.use(chaiHttp);

describe('Test for authenticated CRUD endpoints (with chai)', () => {
  // Runs once before the first test in this block
  before((done) => {
    console.log('\x1b[34m%s', 'Test: Register user and login to obtain JWT');
    // Register request
    const user = {
      user_name: 'test',
      user_email: 'ggg@gmail.com',
      user_address: '@where',
      user_mobile: '0988767666',
      user_password: '123',
    };
    chai.request(app)
      .post('/users')
      // Send user registration details
      .send(user)
      .end((err, res) => {
        res.should.have.status(200);
        res.body.should.be.a('object');
        res.body.should.have.property('returnCode').eql('200');
        res.body.should.have.property('detail').eql('success');
        this.userID = res.body.userID;
        // console.log(this.userID);
        // Follow up with a login
        chai.request(app)
          .post('/users/login')
          .send({
            user_name: 'test',
            user_password: '123',
          })
          // eslint-disable-next-line no-shadow
          .end((err, res) => {
            // console.log('This runs the login part');
            res.should.have.status(200);
            res.body.should.be.a('object');
            res.body.should.have.property('returnCode').eql('200');
            res.body.should.have.property('detail').eql('login successfully');
            res.body.should.have.property('token');
            this.token = res.body.token;
            // console.log(this.token);
            done();
          });
      });
  });
  // Runs once after the last test in this block
  after((done) => {
    console.log('\x1b[34m%s', 'Test: Delete Testing user');
    // Obtain userID from chai 'before' function
    const userid = this.userID;
    // console.log(`delete userid: ${userid}`);
    // console.log(`Delete: ${this.token}`);
    chai.request(app)
      .delete('/users')
      // Send user registration details
      .set('authorization', `Bearer ${this.token}`)
      .send({ user_id: userid.toString() })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.should.be.a('object');
        res.body.should.have.property('returnCode').eql('200');
        res.body.should.have.property('detail').eql('success');
        // console.log(userID);
        done();
      });
  });
  describe('--- Unit test Start ---', () => {
    // Unit test JWT GET method
    it('It should GET all the users with JWT', (done) => {
      // Follow up with requesting user protected page
      // console.log(`Get: ${this.token}`);
      chai.request(app)
        .get('/users')
        .set('authorization', `Bearer ${this.token}`)
        .end((err, res) => {
          res.should.have.status(200);
          res.body.should.be.a('object');
          res.body.should.have.property('returnCode').eql('200');
          res.body.detail.should.be.a('array');
          done();
        });
    });
  });

  //   describe('', () => {
  //     it('It should GET only one specific user', (done) => {
  //       chai.request(app)
  //         .get('/users/1')
  //         .end((err, res) => {
  //           res.should.have.status(200);
  //           res.body.should.be.a('object');
  //           res.body.should.have.property('returnCode').eql('200');
  //           res.body.detail.should.be.a('array');
  //           done();
  //         });
  //     });
  //   });
  //   describe('', () => {
  //     it('It should not GET detail if user id is not existed', (done) => {
  //       chai.request(app)
  //         .get('/users/-1')
  //         .end((err, res) => {
  //           res.should.have.status(200);
  //           res.body.should.be.a('object');
  //           res.body.should.have.property('returnCode').eql('200');
  //           res.body.detail.should.be.a('string');
  //           done();
  //         });
  //     });
  //   });

  //   // Unit test POST method
  //   describe('', () => {
  //     it('It should POST a user', (done) => {
  //       const user = {
  //         user_name: 'I am a test',
  //         user_email: 'ggg@gmail.com',
  //         user_address: '@where',
  //         user_mobile: '0988767666',
  //         user_password: '123',
  //         // login_time: '2009-10-04 22:23:00',
  //         // login_ip: '192.167.1.1',
  //         // create_time: '2009-10-04 22:23:00',
  //         // role_id: '3',
  //       };
  //       chai.request(app)
  //         .post('/users')
  //         .send(user)
  //         .end((err, res) => {
  //           res.should.have.status(200);
  //           res.body.should.be.a('object');
  //           res.body.should.have.property('returnCode').eql('200');
  //           res.body.should.have.property('detail').eql('success');
  //           done();
  //         });
  //     });
  //   });

//   describe('', () => {
//     it('It should not POST a user', (done) => {
//       const user = {
//         user_name: 'I am a test',
//         // user_email: 'ggg@gmail.com',
//         user_address: '@where',
//         user_mobile: '0988767666',
//         user_password: '123',
//         login_time: '2009-10-04 22:23:00',
//         login_ip: '192.167.1.1',
//         create_time: '2009-10-04 22:23:00',
//         role_id: '3',
//       };
//       chai.request(app)
//         .post('/users')
//         .send(user)
//         .end((err, res) => {
//           res.should.have.status(500);
//           res.body.should.be.a('object');
//           res.body.should.have.property('returnCode').eql('500');
//           res.body.should.have.property('detail').eql('error');
//           done();
//         });
//     });
//   });
  // Unit test PATCH method
  // Unit test DELETE method
  // Unit test Login
});
