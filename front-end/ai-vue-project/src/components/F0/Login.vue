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
            <label for="UserName">帳號</label>
            <input id="UserName" type="text" />
          </div>
          <div class="inputBox">
            <label for="passWord">密碼</label>
            <input id="passWord" type="password" />
          </div>
          <p class="remindText">
            尚未成為會員 ?
            <router-link class="loginLink" :to="{ name: 'Signup' }"
              >註冊</router-link
            >
            <a
              class="resetLink"
              href="#"
              @click.prevent="$bvModal.show('myModal'), (showResetBox = true)"
              >/忘記密碼</a
            >
          </p>
          <button class="btn loginBtn" type="button" @click="login">
            Login
          </button>
        </div>
        <b-modal id="myModal" hide-footer>
          <template #modal-title> 重設密碼 </template>
          <div v-if="showResetBox">
            <div class="resetBox">
              <h6>請填寫您的會員信箱</h6>
              <input type="text" />
            </div>
            <b-button class="mt-3" block @click="showResetBox = false"
              >送出</b-button
            >
          </div>
          <div v-if="!showResetBox">
            <div class="resetBox">
              <p>
                密碼重設信已送至您的註冊信箱。請點擊信中連結，重新設定密碼。
              </p>
            </div>
            <b-button class="mt-3" block @click="$bvModal.hide('myModal')"
              >關閉</b-button
            >
          </div>
        </b-modal>
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
      showResetBox: false,
    };
  },
  methods: {
    login() {
      this.$router.push({ name: 'AIA000' });
    },
  },
};
</script>

<style scoped>
h2 {
  font-weight: bold;
  font-size: 1.75rem;
  letter-spacing: 0.2rem;
  margin-top: 60px;
  margin-bottom: 3vh;
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
  padding: 0;
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
  text-align: left;
  padding-left: 5vw;
  margin-bottom: 3px;
}

.inputBox > input {
  background-color: rgb(245, 245, 245);
  border: none;
  border-radius: 3px;
  margin-bottom: 3vh;
  padding: 0px 8px;
  transition: 0.1s;
}

.inputBox > input:focus {
  background-color: white;
  border: #0b346e 1px solid;
}

.loginLink {
  color: #f75c2f;
  font-weight: bold;
}

.loginLink:active,
.loginLink:hover {
  color: #ff9d82;
}

.modalSize {
  width: 450px;
}

.resetBox {
  margin-top: 3vh;
}

.resetBox > input {
  width: 35vh;
  background-color: #eee;
  border-radius: 3px;
  margin-bottom: 3vh;
  padding: 0px 8px;
  transition: 0.1s;
}

.resetBox > p {
  text-align: left;
  font-size: 1rem;
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
  display: block;
  padding-top: 1.5vh;
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
    padding-left: 10vw;
  }

  .inputBox > input {
    width: 70vw;
  }

  .remindText {
    font-size: 1.2rem;
    text-align: right;
    padding-right: 10vw;
  }

  .loginBtn {
    font-size: 1.2rem;
    width: 30vw;
    margin: 5vh 0;
  }
}
</style>
