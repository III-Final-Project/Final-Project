<!-- 
 Page : Signup.vue
 Author : Jyun, Michael
 Time: 2021-04-12
 Desc: build signUp component.
 Desc: Michael revise certification function.
 -->
<template>
  <div class="main">
    <Header />
    <div class="container">
      <div class="picBox"></div>
      <div class="signUpBox" v-show="status == 'sign'">
        <h2>建立您的帳戶</h2>
        <div>
          <div class="inputBox">
            <label for="userName"
              ><span v-if="!userNameCheck">*</span>Username</label
            >
            <input
              id="userName"
              :class="{ error: v.userName }"
              type="text"
              v-model="userName"
            />
            <div class="verify" v-show="v.userName">
              <img
                :src="require('@/assets/icon/exclamationMark.jpg')"
                alt="exclamationMark"
              />
              <span>請輸入使用者名稱</span>
            </div>
          </div>
          <div class="inputBox">
            <label for="passWord"
              ><span v-if="!passWordCheck">*</span>Password</label
            >
            <input
              id="passWord"
              :class="{ error: v.passWord }"
              type="password"
              v-model="passWord"
            />
            <div class="verify" v-show="v.passWord">
              <img
                :src="require('@/assets/icon/exclamationMark.jpg')"
                alt="exclamationMark"
              />
              <span>請輸入密碼</span>
            </div>
          </div>
          <div class="inputBox">
            <label for="pwdCheck"
              ><span v-if="!pwdDoubleCheck">*</span>Password Check</label
            >
            <input
              id="pwdCheck"
              :class="{ error: v.pwdCheck }"
              type="password"
              v-model="pwdCheck"
            />
            <div class="verify" v-show="v.pwdCheck">
              <img
                :src="require('@/assets/icon/exclamationMark.jpg')"
                alt="exclamationMark"
              />
              <span>請輸入二次密碼</span>
            </div>
          </div>
          <div class="inputBox">
            <label for="email"><span v-if="!emailCheck">*</span>Email</label>
            <input
              id="email"
              :class="{ error: v.email }"
              type="text"
              v-model="email"
            />
            <div class="verify" v-show="v.email">
              <img
                :src="require('@/assets/icon/exclamationMark.jpg')"
                alt="exclamationMark"
              />
              <span>請輸入正確的email格式</span>
            </div>
          </div>
          <div class="inputBox">
            <label for="address"
              ><span v-if="!addressCheck">*</span>Address</label
            >
            <input
              id="address"
              :class="{ error: v.address }"
              type="text"
              v-model="address"
            />
            <div class="verify" v-show="v.address">
              <img
                :src="require('@/assets/icon/exclamationMark.jpg')"
                alt="exclamationMark"
              />
              <span>請輸入住址</span>
            </div>
          </div>
          <div class="inputBox">
            <label for="phone"
              ><span v-if="!phoneCheck">*</span>Phone Number</label
            >
            <input
              id="phone"
              :class="{ error: v.phone }"
              type="text"
              v-model="phone"
            />
            <div class="verify" v-show="v.phone">
              <img
                :src="require('@/assets/icon/exclamationMark.jpg')"
                alt="exclamationMark"
              />
              <span>請輸入手機(09xxxx)</span>
            </div>
          </div>
          <p class="remindText">
            Already have account ?
            <router-link class="loginLink" :to="{ name: 'Login' }"
              >Log In</router-link
            >
          </p>
          <button class="loginBtn" @click="signUp">Submit</button>
        </div>
      </div>
      <div class="signUpBox" v-show="status == 'verify'">
        <h2>請輸入Email或簡訊驗證碼</h2>
        <div>
          <div class="inputBox">
            <label for="cfNumber">Certificate Number</label>
            <input id="cfNumber" type="text" v-model="cfNumber" />
          </div>
          <p class="remindText">
            Can't get certificate number ?
            <router-link class="loginLink" to="" @click.prevent="sendSMS"
              >Send again</router-link
            >
          </p>
          <button class="loginBtn" @click="verify">Verify</button>
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
  data() {
    return {
      // 使用者資訊
      userName: '',
      passWord: '',
      pwdCheck: '',
      address: '',
      email: '',
      phone: '',
      cfNumber: '', // 簡訊驗證碼
      status: 'sign', // 頁面狀態
      // 驗證提醒變數
      v: {
        userName: false,
        passWord: false,
        pwdCheck: false,
        address: false,
        email: false,
        phone: false,
      },
    };
  },
  methods: {
    signUp() {
      if (!this.userNameCheck) {
        this.v.userName = true;
      } else {
        this.v.userName = false;
      }
      if (!this.passWordCheck) {
        this.v.passWord = true;
      } else {
        this.v.passWord = false;
      }
      if (!this.pwdDoubleCheck) {
        this.v.pwdCheck = true;
      } else {
        this.v.pwdCheck = false;
      }
      if (!this.emailCheck) {
        this.v.email = true;
      } else {
        this.v.email = false;
      }
      if (!this.addressCheck) {
        this.v.address = true;
      } else {
        this.v.address = false;
      }
      if (!this.phoneCheck) {
        this.v.phone = true;
      } else {
        this.v.phone = false;
      }
      if (
        !this.v.userName &&
        !this.v.passWord &&
        !this.v.pwdDoubleCheck &&
        !this.v.email &&
        !this.v.address &&
        !this.v.phone
      ) {
        this.status = 'verify';
      }
    },
    verify() {
      const newUserObjec = {};
      newUserObjec.username = this.userName;
      newUserObjec.password = this.passWord;
      newUserObjec.email = this.email;
      newUserObjec.phone = this.phone;
      // TODO $axios.post取得驗證碼後若成功兩秒跳轉至登入頁面
      this.$bvToast.toast('註冊成功，請稍候!', {
        title: '註冊訊息',
        variant: 'success',
        solid: true,
      });
      setTimeout(() => {
        this.$router.push({ name: 'Login' });
      }, 2000);
    },
  },
  computed: {
    userNameCheck() {
      return (
        this.userName.length !== 0 &&
        this.userName.trim() !== '' &&
        this.userName != null
      );
    },
    passWordCheck() {
      return (
        this.passWord.length !== 0 &&
        this.passWord.trim() !== '' &&
        this.passWord != null
      );
    },
    pwdDoubleCheck() {
      return this.pwdCheck.trim() !== '' && this.passWord === this.pwdCheck;
    },
    emailCheck() {
      const regex = new RegExp(
        '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Za-z]{2,4}',
      );
      return regex.test(this.email);
    },
    addressCheck() {
      return (
        this.address.length !== 0 &&
        this.address.trim() !== '' &&
        this.address != null
      );
    },
    phoneCheck() {
      const regex = new RegExp('09+[0-9]{8}$');
      return regex.test(this.phone);
    },
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
  padding: 0;
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
  overflow: scroll;
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
  box-sizing: border-box;
  width: 24vw;
  height: 5vh;
  letter-spacing: 1px;
  color: #555;
}

.inputBox > input:focus {
  background-color: white;
  border: #0b346e 2px solid;
}

.inputBox > input.error {
  border: #d93025 2px solid;
}

.inputBox > img {
  width: 20px;
  height: 20px;
}

.inputBox > label > span {
  color: red;
}

.inputBox > .verify {
  text-align: left;
  padding-left: 5vw;
  margin-bottom: 0.5vw;
}

.inputBox > .verify > img {
  width: 20px;
  height: 20px;
}

.inputBox > .verify > span {
  color: #d93025;
  font-size: 0.8rem;
  text-align: left;
  letter-spacing: 1px;
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
