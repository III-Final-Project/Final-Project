<!-- 
 Page : Reset.vue
 Author : Jyun
 Time: 2021-04-25
 Desc: build password resetting component.
 -->
<template>
  <div class="main">
    <div class="picArea">
      <p class="topic">AIFASER</p>
    </div>
    <div class="pwdArea">
      <div class="pwdBox">
        <h4>重設密碼</h4>
        <div class="inputArea">
          <input
            type="password"
            placeholder="請輸入新密碼"
            :class="{ error: v.newPwd }"
            v-model="newPwd"
            @keyup.enter="verify"
          />
          <div class="verify" v-if="v.newPwd">
            <img :src="require('@/assets/icon/alarm.png')" alt="alarm" />
            <span>請輸入有效的密碼</span>
          </div>
          <input
            type="password"
            placeholder="請再次輸入新密碼"
            :class="{ error: v.newPwdCheck }"
            v-model="newPwdCheck"
            @keyup.enter="verify"
          />
          <div class="verify" v-if="v.newPwdCheck">
            <img :src="require('@/assets/icon/alarm.png')" alt="alarm" />
            <span>與上列輸入密碼不相符</span>
          </div>
          <button class="resetBtn" @click="verify">設定新密碼</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Reset',
  data() {
    return {
      newPwd: '',
      newPwdCheck: '',
      v: {
        newPwd: false,
        newPwdCheck: false,
      },
    };
  },
  methods: {
    verify() {
      if (!this.pwdCheck) {
        this.v.newPwd = true;
      } else {
        this.v.newPwd = false;
      }
      if (!this.pwdDolCheck) {
        this.v.newPwdCheck = true;
      } else {
        this.v.newPwdCheck = false;
      }
    },
  },
  computed: {
    pwdCheck() {
      return (
        this.newPwd.length !== 0 &&
        this.newPwd.trim() !== '' &&
        this.newPwd != null
      );
    },
    pwdDolCheck() {
      return this.newPwdCheck === this.newPwd;
    },
  },
};
</script>

<style scoped lang="scss">
.main {
  width: 100vw;
  height: 100vh;
  display: flex;
}

.picArea {
  display: flex;
  justify-content: center;
  align-items: center;
  flex: 1;
  background-color: rgb(48, 45, 51);
  .topic {
    font-size: 6rem;
  }
}

.pwdArea {
  flex: 1;
  background: linear-gradient(to top, #f0e9ed, #c180d3);
  display: flex;
  justify-content: center;
  align-items: center;
}

.pwdBox {
  width: auto;
  height: auto;
  background-color: rgba(255, 255, 255, 0.75);
  padding: 30px 40px;
  > h4 {
    text-align: center;
    margin-bottom: 20px;
  }
}

.inputArea {
  input {
    box-sizing: border-box;
    width: 220px;
    height: 35px;
    display: block;
    border-radius: 3px;
    border: 1px solid rgb(196, 196, 196);
    padding: 0 8px;
    margin: 10px 0;
    &:hover {
      box-shadow: 0 1px 2px rgb(196, 196, 196);
    }
    &:focus {
      box-shadow: 0 1px 3px rgb(166, 166, 167);
    }
  }
  .error {
    border: rgb(250, 77, 77) 1px solid;
  }
  .verify {
    img {
      width: 10px;
      height: 10px;
    }
    span {
      text-align: left;
      font-size: 10px;
    }
  }
}

.resetBtn {
  font: {
    weight: bold;
    family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande',
      'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  }
  width: 220px;
  height: 35px;
  margin: 10px 0;
  border: none;
  outline: none;
  color: white;
  border-radius: 3px;
  background-color: #662377;
  transition: 0.2s;
}

.resetBtn:focus,
.resetBtn:hover {
  background-color: #a82973;
  transform: translate(0, 2px);
}
</style>
