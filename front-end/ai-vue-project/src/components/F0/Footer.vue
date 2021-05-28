<!-- 
 Page : Footer.vue
 Author : Jyun
 Time: 2021-04-12
 Desc:build footer component.
 -->
<template>
  <div class="footerArea">
    <div class="container">
      <div class="foContents">
        <div class="foSlogan">關於我們</div>
        <ul>
          <li>1</li>
          <li>2</li>
        </ul>
      </div>
      <div class="foContents">
        <div class="foSlogan">聯絡我們</div>
        <ul class="foAuthors">
          <a href="https://github.com/Michael-Yan-wun">
            <li>
              <img src="@/assets/icon/githubLogo.png" alt="Github" />
              Michael
            </li>
          </a>
          <a href="https://github.com/jeff14994">
            <li>
              <img src="@/assets/icon/githubLogo.png" alt="Github" />
              Jeff
            </li>
          </a>
          <a href="https://github.com/CZJoanna">
            <li>
              <img src="@/assets/icon/githubLogo.png" alt="Github" />
              Jyun
            </li>
          </a>
          <a href="https://github.com/lucky60232">
            <li>
              <img src="@/assets/icon/githubLogo.png" alt="Github" />
              Jiaer
            </li>
          </a>
        </ul>
      </div>
    </div>
    <div class="copyRight">©2021 AI Final-Project</div>
  </div>
</template>

<script>
export default {
  name: 'Footer',
};
</script>

<style scoped lang="scss">
.footerArea {
  position: relative;
  bottom: 0;
  padding: 0;
  background-color: rgba(33, 33, 33, 0.95);
}

.container {
  display: flex;
  justify-content: space-between;
  padding: 1vh 10vw;
}

.foContents {
  width: 20vw;
  li {
    padding: 5px 0;
    letter-spacing: 1.5px;
  }
}

.foAuthors {
  a {
    color: white;
    &:hover {
      color: #f75c2f;
    }
  }
  li {
    &:hover {
      color: #f75c2f;
    }
  }
  img {
    display: inline-block;
    height: 15px;
    padding-right: 15px;
  }
}

.foSlogan {
  color: white;
  letter-spacing: 2px;
  padding: 5px 0;
}

.copyRight {
  color: white;
  text-align: center;
  padding-bottom: 10px;
}

@media screen and (max-width: 667px) and (-webkit-min-device-pixel-ratio: 2) {
  .foContents {
    width: 30vw;
  }
}
</style>
