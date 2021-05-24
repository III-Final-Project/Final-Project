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
    <div class="myContainer">
      <div class="picBox">
        <div>
          <img src="~@/assets/icon/signUp.png" alt="" />
          <p>Sign Up</p>
        </div>
      </div>
      <div class="signUpBox" v-show="status == 'sign'">
        <h2>建立您的帳戶</h2>
        <div>
          <div class="inputBox">
            <label for="userName"
              ><span v-if="!userNameCheck">*</span>帳號</label
            >
            <input
              id="userName"
              :class="{ error: v.userName }"
              type="text"
              v-model="userName"
              @keypress.enter="signUp"
            />
            <!-- <div class="verify" v-show="!usedNameCheck">
              <span>此帳號已經有人使用</span>
            </div> -->
            <div class="verify" v-show="v.userName">
              <img :src="require('@/assets/icon/alarm.png')" alt="alarm" />
              <span>請輸入有效帳號</span>
            </div>
          </div>
          <div class="inputBox">
            <label for="passWord"
              ><span v-if="!passWordCheck">*</span>密碼</label
            >
            <input
              id="passWord"
              :class="{ error: v.passWord }"
              type="password"
              v-model.lazy="passWord"
              @keypress.enter="signUp"
            />
            <div class="verify" v-show="v.passWord">
              <img :src="require('@/assets/icon/alarm.png')" alt="alarm" />
              <span>請輸入密碼</span>
            </div>
          </div>
          <div class="inputBox">
            <label for="pwdCheck"
              ><span v-if="!pwdDoubleCheck">*</span>再次輸入密碼</label
            >
            <input
              id="pwdCheck"
              :class="{ error: v.pwdCheck }"
              type="password"
              v-model.lazy="pwdCheck"
              @keypress.enter="signUp"
            />
            <div class="verify" v-show="v.pwdCheck">
              <img :src="require('@/assets/icon/alarm.png')" alt="alarm" />
              <span>密碼與上述不符，請再次確認</span>
            </div>
          </div>
          <div class="inputBox">
            <label for="email"><span v-if="!emailCheck">*</span>信箱</label>
            <input
              id="email"
              :class="{ error: v.email }"
              type="text"
              v-model="email"
              @keypress.enter="signUp"
            />
            <div class="verify" v-show="v.email">
              <img :src="require('@/assets/icon/alarm.png')" alt="alarm" />
              <span>請輸入正確的信箱格式</span>
            </div>
          </div>
          <div class="inputBox">
            <label for="address"><span v-if="!addressCheck">*</span>地址</label>
            <input
              id="address"
              :class="{ error: v.address }"
              type="text"
              v-model="address"
              @keypress.enter="signUp"
            />
            <div class="verify" v-show="v.address">
              <img :src="require('@/assets/icon/alarm.png')" alt="alarm" />
              <span>請輸入住址</span>
            </div>
          </div>
          <div class="inputBox">
            <label for="phone"><span v-if="!phoneCheck">*</span>手機號碼</label>
            <input
              id="phone"
              :class="{ error: v.phone }"
              type="text"
              v-model="phone"
              @keypress.enter="signUp"
            />
            <div class="verify" v-show="v.phone">
              <img :src="require('@/assets/icon/alarm.png')" alt="alarm" />
              <span>手機號碼格式(09)或長度錯誤</span>
            </div>
          </div>
          <div class="profileBox">
            <label class="uploadBtn" for="selectedFile">
              ☞ 上傳您的個人照 ☜
              <input id="selectedFile" type="file" @change="onChange"
            /></label>
            <div class="showProfile" v-show="image">
              <img :src="image" alt="in prograss..." />
            </div>
          </div>
          <div class="fotoText">
            <p>相片格式說明</p>
            <p>支援規格：jpg、jpeg、png、heic</p>
            <p>檔案大小限制：1KB至6MB</p>
          </div>
          <p class="remindText">
            已經註冊?
            <router-link class="loginLink" :to="{ name: 'Login' }"
              >登入</router-link
            >
          </p>
          <button class="loginBtn" @click="signUp">註冊</button>
        </div>
      </div>
      <div class="signUpBox cfArea" v-if="status == 'verify'">
        <h2>請輸入簡訊驗證碼</h2>
        <div>
          <div class="inputBox">
            <label for="cfNumber"></label>
            <input id="cfNumber" type="text" v-model="cfNumber" />
          </div>
          <p class="remindText">
            還沒收到驗證碼?
            <router-link class="loginLink" to="" @click.prevent="sendSMS"
              >再寄一次</router-link
            >
          </p>
          <button class="loginBtn" @click="verify">送出</button>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
// import axios from 'axios';
import heic2any from 'heic2any';
import Header from '@/components/F0/Header';
import Footer from '@/components/F0/Footer';
import User from '../../service/user';
import Face from '../../service/face';

export default {
  name: 'Signup',
  components: {
    Header,
    Footer,
  },
  data() {
    return {
      // TODO重複帳號
      // // 會員資料
      // memberNames: [],
      // 使用者資訊
      userName: '',
      passWord: '',
      pwdCheck: '',
      address: '',
      email: '',
      phone: '',
      cfNumber: '', // 簡訊驗證碼-使用者
      cfNumberSms: '', // 簡訊驗證碼-後端系統
      status: 'sign', // 頁面狀態
      // 驗證提醒變數
      v: {
        userName: false,
        // usedName: false,
        passWord: false,
        pwdCheck: false,
        address: false,
        email: false,
        phone: false,
      },
      // 相片檔案
      file: '',
      // 過濾相片規格
      fileFilter: { type: false, size: false },
      image: '',
    };
  },
  // TODO重複帳號
  // mounted() {
  //   User.queryUsers.then((res) => {
  //     if (res.data.returnCode === '200') {
  //       res.data.detail.forEach((member) => {
  //         this.memberNames.push(member.user_name);
  //       });
  //     }
  //   });
  // },
  methods: {
    signUp() {
      if (!this.userNameCheck) {
        this.v.userName = true;
      } else {
        this.v.userName = false;
      }
      // TODO重複帳號
      // if (!this.usedNameCheck) {
      //   this.v.usedName = true;
      // } else {
      //   this.v.usedName = false;
      // }
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
        // TODO重複帳號
        // !this.v.usedName &&
        !this.v.passWord &&
        !this.v.pwdDoubleCheck &&
        !this.v.email &&
        !this.v.address &&
        !this.v.phone
      ) {
        // User.userSMS({ telephone: this.phone }).then((res) => {
        //   if (res.data.returnCode === '200') {
        //     this.cfNumberSms = res.data.detail;
        //     this.status = 'verify';
        //   }
        // });
        this.status = 'verify';
      }
    },
    verify() {
      if (this.cfNumber === this.cfNumberSms) {
        const userObj = {};
        userObj.user_name = this.userName;
        userObj.user_password = this.passWord;
        userObj.user_email = this.email;
        userObj.user_address = this.address;
        userObj.user_mobile = this.phone;
        if (this.file !== '') {
          const imageForm = new FormData();
          imageForm.append('image', this.file);
          Face.imgUpload(imageForm).then((res) => {
            if (res.data.returnCode === '200') {
              User.createUsers(userObj).then((resp) => {
                if (resp.data.returnCode === '200') {
                  this.$bvToast.toast('註冊成功，請稍候!', {
                    title: '註冊訊息',
                    variant: 'success',
                    solid: true,
                  });
                  setTimeout(() => {
                    this.$router.push({ name: 'Login' });
                  }, 2000);
                }
              });
            }
          });
        } else {
          User.createUsers(userObj).then((resp) => {
            if (resp.data.returnCode === '200') {
              this.$bvToast.toast('註冊成功，請稍候!', {
                title: '註冊訊息',
                variant: 'success',
                solid: true,
              });
              setTimeout(() => {
                this.$router.push({ name: 'Login' });
              }, 2000);
            }
          });
        }
      } else {
        this.$bvToast.toast('註冊失敗，請確認驗證碼是否正確!', {
          title: '註冊訊息',
          variant: 'danger',
          solid: true,
        });
      }
    },
    onChange(e) {
      const reader = new FileReader(); // 建立FileReader 監聽 Load 事件
      const files = e.target.files; // 一個檔案流 FileList {0: File, length: 1}
      const file = files[0]; // Bolb物件
      // 判斷副檔名
      if (!file.type.match('image/jpeg|image/png|image/jpg|image/heic')) {
        this.fileFilter.type = false;
        this.$bvToast.toast('檔案不符合支援規格', {
          title: '相片規格有誤',
          variant: 'danger',
          solid: true,
        });
      } else {
        this.fileFilter.type = true;
        // 檔案符合格式後接續判斷檔案尺寸
        // 畫素小於1KB
        if (file.size < 1000) {
          this.fileFilter.size = false;
          this.$bvToast.toast('檔案過小', {
            title: '相片尺寸有誤',
            variant: 'danger',
            solid: true,
          });
        } else if (file.size > 6000000) {
          this.fileFilter.type = false;
          this.$bvToast.toast('檔案過大', {
            title: '相片尺寸有誤',
            variant: 'danger',
            solid: true,
          });
        } else {
          this.fileFilter.size = true;
        }
      }

      // 建立符合格式的檔案
      if (this.fileFilter.type && this.fileFilter.size) {
        if (file.type === 'image/heic') {
          heic2any({
            blob: file,
            toType: 'image/jpeg',
            quality: 0.5,
          }).then((res) => {
            const myBlob = res;
            const blobToFile = new File([myBlob], `${this.userName}.jpg`, {
              type: 'image/jpeg',
            });
            // 轉檔完畢->jpeg
            this.file = blobToFile;
            // 把照片呈現在瀏覽器上
            reader.addEventListener('load', this.imageLoader);
            reader.readAsDataURL(this.file);
          });
        } else {
          // jpg\jpep\png
          this.file = file;
          reader.addEventListener('load', this.imageLoader);
          reader.readAsDataURL(this.file);
        }
      } else {
        this.file = '';
      }
    },
    imageLoader(event) {
      this.image = event.target.result;
    },
  },
  computed: {
    // TODO重複帳號
    // usedNameCheck() {
    //   return !this.memberNames.includes(this.userName);
    // },
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
      const regex = new RegExp('[A-Za-z0-9._%+-]+@[A-Za-z0-9]+.[A-Za-z]{2,4}');
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

<style scoped lang="scss">
h2 {
  font: {
    size: 1.75rem;
    weight: bold;
  }
  margin: 3vh 0;
  letter-spacing: 0.2rem;
}

.main {
  padding-top: 15vh;
  background: linear-gradient(to top, #16222a, #8a215e);
}

.myContainer {
  width: 70vw;
  height: 80vh;
  display: flex;
  margin: 0 auto 8vh auto;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.4);
}

.picBox {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  div {
    text-align: center;
    img {
      width: 15vw;
      margin: 0 auto;
    }
    p {
      padding-top: 7vh;
      color: white;
      font-size: 25px;
      letter-spacing: 5px;
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
  padding-bottom: 2vh;
  > label {
    display: block;
    color: rgb(95, 94, 94);
    text-align: left;
    padding-left: 5.5vw;
    margin-bottom: 3px;
    > span {
      color: red;
    }
  }
  > input {
    background-color: rgb(245, 245, 245);
    border: none;
    border-radius: 3px;
    padding: 0px 8px;
    transition: 0.1s;
    box-sizing: border-box;
    width: 24vw;
    height: 44px;
    letter-spacing: 1px;
    color: #555;
    &:focus {
      background-color: white;
      border: #662377 1px solid;
    }
  }
  .error {
    border: #e94236 1px solid;
  }
  > img {
    width: 20px;
    height: 20px;
  }
  > .verify {
    text-align: left;
    padding-left: 5.7vw;
    > img {
      width: 15px;
      height: 15px;
    }
    > span {
      color: #d93025;
      font-size: 0.8rem;
      text-align: left;
      letter-spacing: 1px;
      padding-left: 5px;
    }
  }
}

.loginLink {
  color: #ef5064;
  font-weight: bold;
  &:focus {
    color: #fa756c;
  }
  &:hover {
    color: #fa756c;
  }
}

.remindText {
  margin: 0;
  text-align: right;
  padding-right: 5.5vw;
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
  background-color: #662377;
  color: white;
  font-weight: bold;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande',
    'Lucida Sans Unicode', 'Geneva', 'Verdana', 'sans-serif';
  outline: none;
  transition: 0.2s;
}

.loginBtn:active,
.loginBtn:hover {
  background-color: #a82973;
  transform: translate(0, 2px);
}

.cfArea {
  padding-top: 10vh;
  h2 {
    font-size: 1.4rem;
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
}

.profileBox {
  text-align: center;
  padding-top: 2vh;
}

.uploadBtn {
  color: rgb(255, 255, 255);
  width: 24vw;
  padding: 10px 0;
  background-color: #ef5064;
  cursor: pointer;
  letter-spacing: 1.5px;
  &:hover {
    background-color: #fa756c;
  }
  &:active {
    background-color: #fa756c;
  }
}

.showProfile {
  width: 24vw;
  border: 1px solid gray;
  border-radius: 3px;
  margin: auto;
  img {
    object-fit: contain;
    max-width: 100%;
    max-height: 35vh;
  }
}

.fotoText {
  width: 24vw;
  margin: auto;
  text-align: left;
  padding: 2vh 0;
  p {
    font-size: 0.8rem;
    margin: 0;
  }
}

#selectedFile {
  display: none;
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

  .myContainer {
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
    > .verify {
      padding-left: 10vw;
    }
  }

  .remindText {
    font-size: 1.15rem;
    padding-right: 10vw;
  }

  .loginBtn {
    font-size: 1.15rem;
    width: 30vw;
  }

  .uploadBtn {
    width: 70vw;
  }

  .showProfile {
    width: 70vw;
  }

  .fotoText {
    width: 70vw;
  }
}
</style>
