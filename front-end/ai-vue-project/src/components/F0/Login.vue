<!-- 
 Page : Login.vue
 Author : Jyun
 Time: 2021-04-12
 Desc: build Login component.
 -->
<template>
  <div class="main">
    <Header />
    <div class="container">
      <div class="picBox"></div>
      <div class="signUpBox">
        <h2>登入您的帳戶</h2>
        <div>
          <div class="inputBox">
            <label for="UserName">Username</label>
            <input id="UserName" type="text" />
          </div>
          <div class="inputBox">
            <label for="passWord">Password</label>
            <input id="passWord" type="password" />
          </div>
          <p class="remindText">
            No account ?
            <router-link class="loginLink" :to="{ name: 'Signup' }"
              >Create one</router-link
            >
          </p>
          <button class="btn loginBtn" type="button">Submit</button>
        </div>
        <a class="resetLink" href="#" @click.prevent="showEmailBox = true"
          >forgot your password?</a
        >
        <div v-if="showEmailBox == true">
          <div class="emailBox">
            <label for="email">Email:</label>
            <input id="email" type="text" />
            <button class="btn resetBtn" type="button">go</button>
          </div>
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
  name: 'Login',
  components: {
    Header,
    Footer,
  },
  data() {
    return {
      showEmailBox: false,
    };
  },
};
</script>

<style scoped>
h2 {
  margin-top: 80px;
  margin-bottom: 10px;
  letter-spacing: 0.2rem;
}

p {
  margin: 0;
  text-align: right;
  padding-right: 5vw;
  font-size: 15px;
}

input {
  box-sizing: border-box;
  width: 25vw;
  height: 6vh;
  font-size: 1.2rem;
  letter-spacing: 1px;
  border: none;
  color: #555;
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

.btn {
  border: none;
  outline: none;
  color: white;
  border-radius: 3px;
  background-color: #0b346e;
  font-weight: bold;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande',
    'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  transition: 0.2s;
}

.picBox {
  flex: 1;
  height: 100vh;
  background-image: url('~@/assets/img/login-sidepic.jpg');
  background-repeat: no-repeat;
  background-position: 50% 10%;
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
  margin-bottom: 3vh;
  padding: 0px 8px;
  transition: 0.1s;
}

.inputBox > input:focus {
  background-color: white;
  border: #0b346e 2px solid;
}

.loginLink {
  color: #f75c2f;
  font-weight: bold;
}

.loginLink:active,
.loginLink:hover {
  color: #ff9d82;
}

.emailBox {
  margin-top: 3vh;
}

.emailBox > input {
  width: 20vw;
  border-bottom: 1px solid rgb(155, 117, 117);
}

.loginBtn {
  width: 10vw;
  height: 40px;
  margin-top: 20px;
  margin-bottom: 20px;
  letter-spacing: 0.5px;
  font-size: 1rem;
}

.resetBtn {
  width: 3vw;
  height: 4vh;
}

.btn:focus,
.btn:hover {
  background-color: #316ec4;
  -moz-box-shadow: 0 7px 6px -6px #5697ec;
  -webkit-box-shadow: 0 7px 6px -6px #5697ec;
  box-shadow: 0 7px 6px -6px #5697ec;
  transform: translate(0, 2px);
}

.resetLink {
  color: black;
  font-weight: bold;
}

.resetLink:hover,
.resetLink:focus {
  color: rgb(95, 95, 95);
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
