<!-- 
 Page : Header.vue
 Author : Jyun
 Time: 2021-04-12
 Desc: build header(navBar) component.
 -->
<template>
  <div id="nav" class="navBar" :class="{ sticky: active == true }">
    <div class="logoBox">
      <router-link :to="{ name: 'AIF000' }"
        ><img class="logo" src="@/assets/icon/teamLogo.png" alt="logo"
      /></router-link>
      <label class="burgerBtn" id="burger" for="menu">☰</label>
    </div>
    <input id="menu" type="checkbox" v-model="checkStatus" />
    <nav class="menu">
      <ul>
        <li class="navLi">
          <a
            class="navLink"
            href="#"
            @click.prevent="scroll('#'), (checkStatus = false)"
            >首頁</a
          >
        </li>
        <li class="navLi">
          <a
            class="navLink"
            href="#vission"
            @click.prevent="scroll('vission'), (checkStatus = false)"
            >使用理念</a
          >
        </li>
        <li class="navLi">
          <a
            class="navLink"
            href="#service"
            @click.prevent="scroll('service'), (checkStatus = false)"
            >服務項目</a
          >
        </li>
        <li class="navLi">
          <a
            class="navLink"
            href="#demo"
            @click.prevent="scroll('demo'), (checkStatus = false)"
            >成果展示</a
          >
        </li>
        <li class="navLi">
          <a
            class="navLink"
            href="#tech"
            @click.prevent="scroll('tech'), (checkStatus = false)"
            >技術一覽</a
          >
        </li>
        <li class="navLi">
          <a
            class="navLink"
            href="#member"
            @click.prevent="scroll('member'), (checkStatus = false)"
            >開發人員</a
          >
        </li>
        <li class="navCut">|</li>
        <li v-if="user_name === 'guest'">
          <router-link class="navLink" :to="{ name: 'Signup' }"
            >註冊</router-link
          >
        </li>
        <li v-if="user_name === 'guest'">
          <router-link class="navLink" :to="{ name: 'Login' }"
            >登入</router-link
          >
        </li>
        <li v-show="user_name !== 'guest'">
          <router-link class="navLink" :to="{ name: 'AIA000' }"
            >後台首頁</router-link
          >
        </li>
        <li v-show="user_name !== 'guest'">
          <router-link class="navLink" to="">{{ user_name }}</router-link>
        </li>
        <li v-show="user_name !== 'guest'">
          <router-link
            class="navLink"
            to=""
            @click.native.prevent.capture="logOut"
            >登出</router-link
          >
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      active: false,
      checkStatus: null,
      user_name: 'guest',
    };
  },
  created() {
    if (this.$store.state.user_name != null) {
      this.user_name = this.$store.state.user_name;
    }
  },
  mounted() {
    window.document.onscroll = () => {
      const nav = document.querySelector('#nav');
      if (window.scrollY > nav.offsetTop) {
        this.active = true;
      } else {
        this.active = false;
      }
    };
  },
  methods: {
    async scroll(spot) {
      if (this.$router.currentRoute.name === 'AIF000') {
        this.scrollToSpot(spot);
      } else {
        await this.$router.push({ name: 'AIF000' });
        this.scrollToSpot(spot);
      }
    },
    scrollToSpot(spot) {
      const vission = document.querySelector('#vission');
      const service = document.querySelector('#service');
      const demo = document.querySelector('#demo');
      const tech = document.querySelector('#tech');
      const member = document.querySelector('#member');
      switch (spot) {
        case 'vission':
          window.scrollTo({ behavior: 'smooth', top: vission.offsetTop });
          break;
        case 'service':
          window.scrollTo({ behavior: 'smooth', top: service.offsetTop });
          break;
        case 'demo':
          window.scrollTo({ behavior: 'smooth', top: demo.offsetTop });
          break;
        case 'tech':
          window.scrollTo({ behavior: 'smooth', top: tech.offsetTop });
          break;
        case 'member':
          window.scrollTo({ behavior: 'smooth', top: member.offsetTop });
          break;
        default:
          window.scrollTo({ behavior: 'smooth', top: 0 });
          break;
      }
    },
    logOut() {
      this.$store.state.user_name = null;
      this.$store.state.accessToken = null;
      if (this.$route.name === 'AIF000') {
        this.$router.go(0);
      } else {
        this.$router.push({ name: 'AIF000' });
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.navBar {
  font: {
    size: 1em;
  }
  z-index: 1;
  display: flex;
  justify-content: space-between;
  width: 100vw;
  height: 9vh;
  background-color: rgba(33, 33, 33, 0.95);
  position: fixed;
  top: 0;
  transition: 300ms;
}

.logo {
  height: 9vh;
  padding-left: 1vw;
  transition: 300ms;
}

.menu {
  margin: 0 25px;
  ul {
    display: flex;
    margin: 0;
  }
  li {
    display: inline-block;
    height: 9vh;
    width: 80px;
    line-height: 9vh;
    text-align: center;
  }
  .navLi {
    margin: 0 25px;
  }
  .navLink {
    display: block;
    color: white;
    &:hover {
      color: #f75c2f;
    }
    &:active {
      color: #f75c2f;
    }
  }
  .navCut {
    width: 15px;
    color: white;
  }
}

.sticky {
  height: 8vh;
  box-shadow: 0px 3px 10px 0px rgba(0, 0, 0, 0.2);
  a {
    height: 8vh;
    line-height: 8vh;
  }
  li {
    height: 8vh;
    line-height: 8vh;
  }
  .navCut {
    height: 8vh;
    line-height: 8vh;
  }
  .logo {
    height: 7.8vh;
    padding-left: 2vw;
    transition: 300ms;
  }
  .burgerBtn {
    height: 8vh;
    line-height: 8vh;
  }
}

#burger,
#menu {
  display: none;
}

@media screen and (max-width: 1100px) and (-webkit-min-device-pixel-ratio: 2) {
  .navBar {
    flex-direction: column;
  }

  .logoBox {
    display: flex;
    justify-content: space-between;
  }

  .burgerBtn {
    color: white;
    padding-right: 8vw;
    line-height: 9vh;
  }

  .menu {
    margin: 0;
    transform: scale(1, 0);
    transform-origin: top;
    transition: transform 0.2s ease-out;
    ul {
      display: block;
    }
    li {
      opacity: 0;
      display: block;
      background-color: rgba(33, 33, 33, 0.95);
      width: 100vw;
      height: 7vh;
      line-height: 7vh;
      padding: 0.1vh 8vw;
      letter-spacing: 3px;
      transition: opacity 0.2s ease-out;
    }
    > ul > li + li {
      border-top: 1px solid rgba(71, 66, 66, 0.7);
    }
    .navLi {
      margin: 0;
    }
    .navLink {
      height: 7vh;
      text-align: left;
    }
    .navCut {
      display: none;
    }
  }

  .sticky a,
  .sticky li,
  .sticky .navCut {
    height: 7vh;
    line-height: 7vh;
  }

  #burger {
    display: block;
  }

  #menu:checked ~ .menu {
    transform: scale(1, 1);
    li {
      opacity: 0.8;
    }
  }
}
</style>
