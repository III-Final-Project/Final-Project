<!-- 
 Page : Signup.vue
 Author : Jyun
 Time: 2021-04-12
 Desc: build signUp component.
 -->
<template>
  <div class="main">
    <Header />
    <div class="container">
      <div class="picBox"></div>
      <div class="signUpBox">
        <h2>建立您的帳戶</h2>
        <div>
          <div class="inputBox">
            <label for="UserName">Username</label>
            <input id="UserName" type="text" />
          </div>
          <div class="inputBox">
            <label for="passWord">Password</label>
            <input id="passWord" type="password" />
          </div>
          <div class="inputBox">
            <label for="pwdCheck">Password Check</label>
            <input id="pwdCheck" type="password" />
          </div>
          <div class="inputBox">
            <label for="email">Email</label>
            <input id="email" type="text" />
          </div>
          <div class="inputBox">
            <label for="phone">Phone Number</label>
            <input id="phone" type="text" />
          </div>
          <p class="remindText">
            Already have account ?
            <router-link class="loginLink" :to="{ name: 'Login' }"
              >Log In</router-link
            >
          </p>
          <button class="loginBtn">Submit</button>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import Header from '@/components/F0/Header';
import Footer from '@/components/F0/Footer';

export default {
  name: 'Signup',
  components: {
    Header,
    Footer,
  },
};
</script>

<style scoped>
h2 {
  margin: 3vh 0;
  letter-spacing: 0.2rem;
}

.main {
  padding-top: 20vh;
  background-color: rgb(15, 15, 54);
}

.container {
  width: 70vw;
  height: 90vh;
  display: flex;
  margin: 0 auto 8vh auto;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 2px 2px 10px 2px gray;
}

.picBox {
  flex: 1;
  height: 100vh;
  background-image: url('~@/assets/img/signup-sidepic.jpg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}

.signUpBox {
  flex: 1;
  text-align: center;
  background-color: white;
}

.logoBox {
  height: 100px;
}

.inputBox > label {
  display: block;
  color: rgb(95, 94, 94);
  font-weight: bold;
  text-align: left;
  padding-left: 5vw;
  margin-bottom: 3px;
}

.inputBox > input {
  background-color: #eee;
  border: none;
  border-radius: 3px;
  margin-bottom: 12px;
  padding: 0px 8px;
  transition: 0.1s;
  font-size: 1.2rem;
  box-sizing: border-box;
  width: 25vw;
  height: 6vh;
  letter-spacing: 1px;
  color: #555;
}

.inputBox > input:focus {
  background-color: white;
  border: #0b346e 2px solid;
}

.loginLink {
  color: #f75c2f;
  font-weight: bold;
}

.loginLink:focus,
.loginLink:hover {
  color: #ff9d82;
}

.remindText {
  margin: 0;
  text-align: right;
  padding-right: 5vw;
  font-size: 15px;
}

.loginBtn {
  width: 10vw;
  height: 40px;
  margin-top: 20px;
  margin-bottom: 20px;
  letter-spacing: 0.5px;
  font-size: 1rem;
  border: none;
  border-radius: 3px;
  background-color: #0b346e;
  color: white;
  font-weight: bold;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande',
    'Lucida Sans Unicode', 'Geneva', 'Verdana', 'sans-serif';
  outline: none;
  transition: 0.2s;
}

.loginBtn:focus,
.loginBtn:hover {
  background-color: #316ec4;
  -moz-box-shadow: 0 7px 6px -6px #5697ec;
  -webkit-box-shadow: 0 7px 6px -6px #5697ec;
  box-shadow: 0 7px 6px -6px #5697ec;
  transform: translate(0, 2px);
}

@media only screen and (min-device-width: 375px) and (max-device-width: 667px) and (-webkit-min-device-pixel-ratio: 2) {
  h2 {
    font-size: 1.6rem;
    margin: 3vh 0;
    letter-spacing: 0.2rem;
  }

  .main {
    padding-top: 15vh;
  }

  .container {
    flex-direction: column;
    width: 90vw;
    height: 82vh;
    box-shadow: 0 0 4px 1px #ddd;
  }

  .picBox {
    display: none;
  }

  .inputBox > label {
    font-size: 1.15rem;
    font-weight: bold;
    padding-left: 10vw;
  }

  .inputBox > input {
    width: 70vw;
  }

  .remindText {
    font-size: 1.2rem;
    text-align: center;
    padding: 0;
  }

  .loginBtn {
    font-size: 1.2rem;
    width: 30vw;
  }
}
</style>
