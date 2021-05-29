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
      <div class="picBox">
        <div>
          <img src="~@/assets/icon/logIn.png" alt="" />
          <p>Log In</p>
        </div>
      </div>
      <div class="signUpBox">
        <h2>登入您的帳戶</h2>
        <div>
          <div class="inputBox">
            <label for="UserName">帳號</label>
            <input id="UserName" type="text" v-model="user_name" />
          </div>
          <div class="inputBox">
            <label for="passWord">密碼</label>
            <input id="passWord" type="password" v-model="user_password" />
          </div>
          <div class="btnArea">
            <button class="btn loginBtn" type="button" @click="login_vuex">
              GO
            </button>
            <p class="remindText">
              尚未成為會員 ?
              <router-link class="loginLink" :to="{ name: 'Signup' }">
                註冊</router-link
              >
              <a
                class="resetLink"
                href="#"
                @click.prevent="$bvModal.show('myModal'), (showResetBox = true)"
                >/忘記密碼</a
              >
            </p>
          </div>
        </div>
        <div class="faceArea">
          <img
            src="@/assets/icon/faceScan.png"
            alt="FaceId"
            @click="$bvModal.show('faceModal')"
          />
          <p>用<span style="color: #fe5987"> Face ID </span> 登入</p>
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
      <b-modal id="faceModal" class="faceModal" hide-footer>
        <template #modal-title> FaceID偵測 </template>
        <Camera @faceVerify="faceVerify" />
      </b-modal>
    </div>
    <Footer />
  </div>
</template>

<script>
import Header from '@/components/F0/Header';
import Footer from '@/components/F0/Footer';
import Camera from '@/components/F0/Camera_F';

export default {
  name: 'Login',
  components: {
    Header,
    Footer,
    Camera,
  },
  data() {
    return {
      showResetBox: false,
      user_name: null,
      user_password: null,
      incorrectAuth: null,
      token: '',
    };
  },
  methods: {
    login_vuex() {
      this.$store
        .dispatch('userLogin', {
          user_name: this.user_name,
          user_password: this.user_password,
        })
        .then(() => {
          this.$router.push({ name: 'AIA000' });
        })
        .catch((err) => {
          if (err) {
            this.incorrectAuth = true;
          }
        });
    },
    login() {
      this.$router.push({
        name: 'AIA000',
        params: { user_name: this.user_name },
      });
    },
    faceVerify(res) {
      if (res !== 'Unknown') {
        this.user_name = res;
        // TODO 利用使用者名稱搜尋使用者帳號與密碼
        this.user_password = '1234';
        // TODO 利用VueX與JWT登入並且記錄使用者資訊
        // this.login_vuex();
        // eslint-disable-next-line
        console.log(`使用者名稱：${this.user_name}`);
        // eslint-disable-next-line
        console.log(`使用者帳號：${this.user_password}`);
        this.login();
      } else {
        this.$bvToast.toast(`請關閉偵測視窗並重新打開，或使用帳號密碼登入`, {
          title: '偵測失敗',
          variant: 'danger',
          solid: true,
        });
      }
    },
  },
};
</script>

<style scoped lang="scss">
$main_color: #c180d3;
$sub_bg_color: #fafbff;
$link_color: #f75c2f;
$link_hover_color: #ff9d82;
$btn_color: #662377;
$btn_hover_color: #a82973;

h2 {
  font: {
    weight: bold;
    size: 1.75rem;
  }
  letter-spacing: 0.2rem;
  margin: 3vh 0;
}

p {
  margin: 0;
  text-align: right;
  font-size: 15px;
}

input {
  box-sizing: border-box;
  width: 24vw;
  height: 44px;
  font-size: 1.2rem;
  letter-spacing: 1px;
  border: none;
  color: #555;
}

.main {
  padding-top: 15vh;
  background-color: $sub_bg_color;
}

.container {
  padding: 0;
  width: 70vw;
  height: 80vh;
  display: flex;
  margin: 0 auto 8vh auto;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.4);
}

.btn {
  font: {
    weight: bold;
    family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande',
      'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  }
  border: none;
  outline: none;
  color: white;
  border-radius: 3px;
  background-color: $btn_color;
  transition: 0.2s;
}

.btn:active,
.btn:hover {
  background-color: $btn_hover_color;
  transform: translate(0, 2px);
}

.picBox {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(to top, #16222a, $main_color);
  div {
    img {
      width: 15vw;
      margin: 0 auto;
    }
    p {
      padding-top: 7vh;
      color: white;
      font-size: 25px;
      letter-spacing: 5px;
      text-align: center;
    }
  }
}

.signUpBox {
  flex: 1;
  text-align: center;
  background-color: white;
  overflow-y: auto;
}

.logoBox {
  height: 100px;
}

.inputBox {
  > label {
    display: block;
    color: rgb(95, 94, 94);
    text-align: left;
    padding-left: 5.5vw;
    margin-bottom: 3px;
  }
  > input {
    background-color: rgb(245, 245, 245);
    border: none;
    border-radius: 3px;
    margin-bottom: 3vh;
    padding: 0px 8px;
    transition: 0.1s;
    &:focus {
      background-color: white;
      border: $btn_color 1px solid;
    }
  }
}

.loginLink {
  color: $link_color;
  font-weight: 500;
  &:active {
    color: $link_hover_color;
  }
  &:hover {
    color: $link_hover_color;
  }
}

.modalSize {
  width: 450px;
}

.faceArea {
  margin: 2vh auto;
  width: 180px;
  height: 180px;
  border-radius: 40%;
  box-shadow: 0 -10px 30px -20px rgba(0, 0, 0, 0.4);
  overflow: hidden;
  cursor: pointer;
  > img {
    margin-top: 2.5vh;
    width: 100px;
    height: 100px;
  }
  > p {
    padding-top: 1vh;
    text-align: center;
  }
}

.modal-body {
  height: 350px;
}

.resetBox {
  margin-top: 3vh;
  > input {
    width: 100%;
    background-color: #eee;
    border-radius: 3px;
    margin-bottom: 3vh;
    padding: 0px 8px;
    transition: 0.1s;
  }
  > p {
    text-align: left;
    font-size: 1rem;
  }
}

.btnArea {
  display: flex;
  justify-content: space-between;
  padding: 0 5.5vw;
}

.remindText {
  margin-left: 3vw;
}

.loginBtn {
  width: 50px;
  height: 50px;
  letter-spacing: 0.5px;
  font-size: 1rem;
  border-radius: 50%;
}

.resetBtn {
  width: 3vw;
  height: 4vh;
}

.resetLink {
  color: black;
  display: block;
  padding-top: 1.5vh;
  &:hover {
    color: rgb(95, 95, 95);
  }
  &:focus {
    color: rgb(95, 95, 95);
  }
}

@media screen and (max-width: 667px) and (-webkit-min-device-pixel-ratio: 2) {
  h2 {
    font-size: 1.6rem;
    margin: 3vh 0;
    letter-spacing: 0.2rem;
  }

  .main {
    padding-top: 13vh;
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

  .inputBox {
    > label {
      font-size: 1.15rem;
      padding-left: 10vw;
    }
    > input {
      width: 70vw;
    }
  }

  .btnArea {
    padding: 0 10vw;
  }

  .loginBtn {
    font-size: 1.2rem;
  }

  .faceArea {
    margin: 5vh auto;
    width: 180px;
    height: 180px;
    > img {
      margin-top: 3vh;
    }
  }
}
</style>
