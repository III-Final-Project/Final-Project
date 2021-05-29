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
        <ul class="foIcons">
          <li>台中資策會</li>
          <li>AI班結訓成果報告</li>
        </ul>
      </div>
      <div class="foContents">
        <div class="foSlogan">聯絡我們</div>
        <ul class="foIcons">
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
$footer_bg_color: rgba(55, 55, 55, 0.95);
$footer_font_color: #eee;

.footerArea {
  position: relative;
  bottom: 0;
  padding: 0;
  background-color: $footer_bg_color;
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
    color: $footer_font_color;
    letter-spacing: 2px;
    font: {
      size: 0.875rem;
      weight: 400;
    }
  }
}

.foIcons {
  a {
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
  padding: 5px 0;
  color: $footer_font_color;
  letter-spacing: 2px;
}

.copyRight {
  text-align: center;
  padding-bottom: 10px;
  color: $footer_font_color;
  font-size: 0.875rem;
  letter-spacing: 2px;
}

@media screen and (max-width: 667px) and (-webkit-min-device-pixel-ratio: 2) {
  .foContents {
    width: 30vw;
  }
}
</style>
