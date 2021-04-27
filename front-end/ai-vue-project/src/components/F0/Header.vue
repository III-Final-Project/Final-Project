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
    <input id="menu" type="checkbox" />
    <nav class="menu">
      <ul>
        <li class="navLi">
          <router-link class="navLink" :to="{ name: 'AIF000' }"
            >首頁</router-link
          >
        </li>
        <li class="navLi"><a class="navLink" href="#vission">使用理念</a></li>
        <li class="navLi"><a class="navLink" href="#service">服務項目</a></li>
        <li class="navLi"><a class="navLink" href="#demo">成果展示</a></li>
        <li class="navLi"><a class="navLink" href="#techView">技術一覽</a></li>
        <li class="navCut">|</li>
        <li>
          <router-link class="navLink" :to="{ name: 'Signup' }"
            >註冊</router-link
          >
        </li>
        <li>
          <router-link class="navLink" :to="{ name: 'Login' }"
            >登入</router-link
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
    };
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
};
</script>

<style scoped>
.navBar {
  z-index: 1;
  display: flex;
  justify-content: space-between;
  width: 100vw;
  height: 13vh;
  background-color: rgb(255, 255, 255);
  font-weight: bold;
  font-size: 1em;
  position: fixed;
  top: 0;
  transition: 300ms;
}

.logo {
  height: 13vh;
  padding-left: 1vw;
  transition: 300ms;
}

.menu {
  margin: 0 25px;
}

.menu ul {
  display: flex;
  margin: 0;
}

.menu li {
  display: inline-block;
  height: 13vh;
  width: 80px;
  line-height: 13vh;
  text-align: center;
}

.menu .navLi {
  margin: 0 25px;
}

.menu .navLink {
  display: block;
  color: rgb(95, 94, 94);
}

.menu .navLink:active,
.menu .navLink:hover {
  color: #f75c2f;
}

.menu .navCut {
  width: 15px;
}

.sticky {
  height: 11vh;
  box-shadow: 0px 3px 10px 0px rgba(0, 0, 0, 0.2);
}

.sticky .logo {
  height: 10.5vh;
  padding-left: 2vw;
  transition: 300ms;
}

.sticky .burgerBtn {
  height: 11vh;
  line-height: 11vh;
}

.sticky a,
.sticky li,
.sticky .navCut {
  height: 11vh;
  line-height: 11vh;
}

#burger,
#menu {
  display: none;
}

@media only screen and (min-device-width: 375px) and (max-device-width: 1024px) and (-webkit-min-device-pixel-ratio: 2) {
  .navBar {
    flex-direction: column;
  }

  .logoBox {
    display: flex;
    justify-content: space-between;
  }

  .burgerBtn {
    padding-right: 8vw;
    line-height: 13vh;
  }

  .menu {
    margin: 0;
    display: none;
  }

  .menu ul {
    display: block;
    background: white;
    border-bottom: 1px solid #ddd;
  }

  .menu li {
    display: block;
    width: 100vw;
    height: 7vh;
    line-height: 7vh;
    padding: 0.1vh 8vw;
    letter-spacing: 3px;
  }

  .menu > ul > li + li {
    border-top: 1px solid rgb(243, 242, 242);
  }

  .menu .navLi {
    margin: 0;
  }

  .menu .navLink {
    height: 7vh;
    color: rgb(95, 94, 94);
    text-align: left;
  }

  .menu .navCut {
    display: none;
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
    display: block;
  }
}
</style>
