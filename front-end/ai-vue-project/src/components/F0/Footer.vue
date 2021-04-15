<!-- 
 Page : Footer.vue
 Author : Jyun
 Time: 2021-04-12
 Desc:build footer component.
 -->
<template>
  <div>
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
          <div class="foSlogan">關於我們</div>
          <ul>
            <li>3</li>
            <li>4</li>
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
  </div>
</template>

<script>
export default {
  name: 'Footer',
};
</script>

<style scoped>
.footerArea {
  border-top: 1px solid rgb(192, 173, 173);
  background-color: #fff;
}

.container {
  display: flex;
  height: 25vh;
  justify-content: space-between;
  margin: 25px 30px;
}

.foContents {
  width: 20vw;
  margin: 0 5vw;
}

.foContents li {
  margin: 15px auto;
}

.foAuthors li:hover,
.foAuthors a:active {
  color: #f75c2f;
}

.foAuthors img {
  display: inline-block;
  height: 15px;
  padding-right: 15px;
}

.foAuthors a {
  color: rgb(95, 94, 94);
  font-weight: bold;
}

.foSlogan {
  font-size: 1.3rem;
  margin-bottom: 5px;
}

.copyRight {
  text-align: center;
  margin-bottom: 10px;
}

@media only screen and (min-device-width: 375px) and (max-device-width: 667px) and (-webkit-min-device-pixel-ratio: 2) {
}
</style>
