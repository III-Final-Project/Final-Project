<!-- 
 Page : AIF000.vue
 Author : Jyun
 Time: 2021-04-19
 Desc: update AIF000 page.
 -->
<template>
  <div class="main">
    <Header />
    <div class="topArea">
      <div class="textBox">
        <p class="topic">為您的客戶量身打造</p>
        <p class="content">使用AIfaser，讓AI成為您推薦商品的好幫手。</p>
        <a class="topBtn" href="#demo">Learn More</a>
      </div>
      <div class="imgBox"></div>
    </div>
    <div class="spot" id="vission"></div>
    <div class="vissionArea box">
      <p class="conTopic">使用理念</p>
      <div class="vissionBox">
        <p class="vissionContent">
          除了『
          店裡最熱門、當今最流行』之外，能透過人工智慧自動判斷客人性別、年齡及衣著類型，來協助店員給出更精準的服飾推薦。
        </p>
      </div>
    </div>
    <div class="spot" id="service"></div>
    <div class="featuresArea box">
      <p class="conTopic">服務項目</p>
      <div class="featBox">
        <div class="featCard">
          <div class="featIcon">
            <img src="@/assets/img/jyun.jpeg" alt="" />
          </div>
          <div class="featText">
            <p class="featTitle">客製化</p>
            <p class="featDescription">
              線上觀賞Netflix（網飛）電影與節目，或直接串流至智慧型電視、遊戲機、PC、Mac、手機、平板電腦等多種裝置。
            </p>
          </div>
        </div>
        <div class="featCard">
          <div class="featIcon">
            <img src="@/assets/img/jyun.jpeg" alt="" />
          </div>
          <div class="featText">
            <p class="featTitle">客製化 隨時隨地</p>
            <p class="featDescription">
              線上觀賞Netflix（網飛）電影與節目，或直接串流至智慧型電視、遊戲機、PC、Mac、手機、平板電腦等多種裝置。
            </p>
          </div>
        </div>
        <div class="featCard">
          <div class="featIcon">
            <img src="@/assets/img/jyun.jpeg" alt="" />
          </div>
          <div class="featText">
            <p class="featTitle">客製化</p>
            <p class="featDescription">
              線上觀賞Netflix（網飛）電影與節目，或直接串流至智慧型電視、遊戲機、PC、Mac、手機、平板電腦等多種裝置。
            </p>
          </div>
        </div>
      </div>
    </div>
    <div class="spot" id="demo"></div>
    <div class="demo box">
      <p class="conTopic">成果展示</p>
    </div>
    <div class="spot" id="tech"></div>
    <div class="techArea box">
      <p class="conTopic">技術一覽</p>
      <div class="techBox">
        <div class="techCard-1">
          <div class="techBanner">
            <div class="techIcon"></div>
            <div class="techTitle">Neutral Networks</div>
          </div>
          <div class="techContent">
            <p class="subTitle">Data preprocessing</p>
            <p>- Numpy</p>
            <p>- Pandas</p>
            <p>- Matplotlib</p>
          </div>
          <div class="techContent">
            <p class="subTitle">Data explore</p>
            <p>- scikit-learn</p>
          </div>
          <div class="techContent">
            <p class="subTitle">Cloud Services</p>
            <p>- Azure</p>
            <p>- Google</p>
          </div>
          <div class="techContent">
            <p class="subTitle">Tensorflow</p>
            <p>- Fashion recommendation algorithm</p>
          </div>
        </div>
        <div class="techCard-2">
          <div class="techBanner">
            <div class="techIcon"></div>
            <div class="techTitle">Web Front-end</div>
          </div>
          <div class="techContent">
            <p class="subTitle">FrameWork</p>
            <p>- Vue.js</p>
          </div>
          <div class="techContent">
            <p class="subTitle">Modules</p>
            <p>- Webpack</p>
            <p>- Webcam</p>
            <p>- Bootstrap</p>
          </div>
          <div class="techContent">
            <p class="subTitle">UI & UX</p>
            <p class="subTitle">SASS</p>
            <p class="subTitle">RWD</p>
          </div>
        </div>
        <div class="techCard-3">
          <div class="techBanner">
            <div class="techIcon"></div>
            <div class="techTitle">Web back-end</div>
          </div>
          <div class="techContent">
            <p class="subTitle">Framework</p>
            <p>- Express</p>
            <p>- Flask</p>
          </div>
          <div class="techContent">
            <p class="subTitle">Modules</p>
            <p>- RESTful API</p>
            <p>- JWT</p>
            <p>- Email & SMS Server</p>
            <p>- Login with Access right system</p>
            <p>- Unit-Test</p>
          </div>
        </div>
        <div class="techCard-4">
          <div class="techBanner">
            <div class="techIcon"></div>
            <div class="techTitle">Databases</div>
          </div>
          <div class="techContent">
            <p>- mongoDB</p>
            <p>- MySQL</p>
          </div>
        </div>
        <div class="techCard-5">
          <div class="techBanner">
            <div class="techIcon"></div>
            <div class="techTitle">SCCS</div>
          </div>
          <div class="techContent">
            <p>- Git</p>
            <p>- GitHub</p>
            <p>- Code Review</p>
            <p>- Coding Style | Airbnb</p>
          </div>
        </div>
      </div>
    </div>
    <!-- 開發人員 -->
    <div class="spot" id="member"></div>
    <div class="memberArea box">
      <p class="conTopic">開發人員</p>
      <div class="memberBox">
        <div class="memberCard">
          <div class="memberProfile">
            <img src="@/assets/img/michael.jpg" alt="michael" />
          </div>
          <div class="memberText">
            <p class="memberTitle">Michael</p>
            <p class="memberSubTitle">前、後端開發</p>
            <p class="memberContent">
              如果debug是將錯誤資源回收, <br />那寫程式一定是亂丟垃圾的過程。
            </p>
          </div>
        </div>
        <div class="memberCard">
          <div class="memberProfile">
            <img src="@/assets/img/jeff.jpg" alt="jeff" />
          </div>
          <div class="memberText">
            <p class="memberTitle">Jeff</p>
            <p class="memberSubTitle">後端開發</p>
            <p class="memberContent">
              世界上可以分成10種人。<br />
              懂二進位的人，以及不懂二進位的人。
            </p>
          </div>
        </div>
        <div class="memberCard">
          <div class="memberProfile">
            <img src="@/assets/img/jyun.jpeg" alt="jyun" />
          </div>
          <div class="memberText">
            <p class="memberTitle">Jyun</p>
            <p class="memberSubTitle">UI&UX、前端開發</p>
            <p class="memberContent">喜歡攝影<br /></p>
          </div>
        </div>
        <div class="memberCard">
          <div class="memberProfile">
            <img src="@/assets/img/jiar.png" alt="jiar" />
          </div>
          <div class="memberText">
            <p class="memberTitle">Jiar</p>
            <p class="memberSubTitle">後端開發</p>
            <p class="memberContent">偶爾畫圖<br />努力學習AI與python</p>
          </div>
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
  name: 'AIF000',
  components: {
    Header,
    Footer,
  },
  mounted() {
    const tooltip = document.querySelectorAll('.tooltip');
    tooltip.forEach((item) => {
      // eslint-disable-next-line
      item.style.display = 'none';
    });
  },
};
</script>

<style scoped lang="scss">
//color
$main_color: #c180d3;
$card_bg_color: #fafbff;
$btn_color: #f75c2f;

//font
@mixin font($size, $weight, $letter-spacing) {
  font: {
    size: $size;
    weight: $weight;
  }
  letter-spacing: $letter-spacing;
}

p {
  margin: 0;
}

.main {
  padding-top: 13vh;
}

// 共同樣式

.spot {
  position: relative;
  top: -8vh;
  display: block;
  visibility: hidden;
}

.box {
  padding: 0 6vw 8vh 6vw;
}

.conTopic {
  padding: 5vh 0;
  letter-spacing: 2px;
  text-align: center;
  @include font(2.2rem, 400, 0);
}

//top

.topArea {
  display: flex;
  height: 87vh;
}

.textBox {
  flex: 1;
  padding: 8vh 6vw;
  .topic {
    padding: 20px 0;
    @include font(3.5rem, 500, 3px);
  }
  .content {
    margin-bottom: 20px;
    padding: 20px 0;
    @include font(1.4rem, 300, 3px);
  }
  .topBtn {
    padding: 12px 25px 12px 25px;
    border-radius: 60px;
    border: white 3px solid;
    background-color: $btn_color;
    color: white;
    transition: 0.35s;
    &:hover {
      border: $btn_color 3px solid;
      background-color: white;
      color: $btn_color;
    }
  }
}

.imgBox {
  flex: 1;
  background: {
    image: url('~@/assets/img/page-mainpic.png');
    size: 85%;
    position: center;
    repeat: no-repeat;
  }
}

//vission

.vissionArea {
  background-color: $card_bg_color;
}

.vissionContent {
  @include font(1.1rem, 300, 1px);
}

//features

.featBox {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  grid-gap: 1.5rem;
}

.featCard {
  width: 100%;
  border-radius: 15px;
  .featIcon {
    width: 120px;
    height: 120px;
    margin: 2rem auto;
    overflow: hidden;
    img {
      max-width: 100%;
    }
  }
  .featText {
    padding: 0 1.5rem;
    .featTitle {
      color: #f75c2f;
      text-align: center;
      @include font(1.3rem, 300, 2px);
    }
    .featDescription {
      padding: 1.3rem 0;
    }
  }
}

//demo

// tech

.techBox {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-template-rows: repeat(6, minmax(50px, 1fr));
  grid-template-areas:
    'neutral neutral front front back back'
    'neutral neutral front front back back'
    'neutral neutral front front back back'
    'neutral neutral front front back back'
    'neutral neutral databases databases sccs sccs'
    'neutral neutral databases databases sccs sccs';
  grid-gap: 1.5rem;
}

.techCard-1 {
  grid-area: neutral;
}

.techCard-2 {
  grid-area: front;
}

.techCard-3 {
  grid-area: back;
}

.techCard-4 {
  grid-area: databases;
}

.techCard-5 {
  grid-area: sccs;
}

.techBanner {
  display: grid;
  grid-auto-flow: column;
  justify-content: start;
  .techIcon {
    width: 10px;
    height: 50px;
    background: linear-gradient(to top, #721b4e, #a82973);
    img {
      max-width: 100%;
    }
  }

  .techTitle {
    line-height: 50px;
    padding-left: 20px;
    @include font(1.5rem, 500, 0px);
  }
}

.techContent {
  padding: 2vh 0;
  .subTitle {
    padding-bottom: 1vh;
    color: #a82973;
    @include font(1.15rem, 300, 1px);
  }
}

div[class*='techCard'] {
  padding: 0 2vw;
  border-radius: 15px;
  background-color: $card_bg_color;
  overflow: hidden;
}

// member

.memberBox {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  grid-gap: 1.5rem;
}

.memberCard {
  min-height: 250px;
  border-radius: 20px;
  background-color: $card_bg_color;
  text-align: center;
  overflow: hidden;
}

.memberProfile {
  width: 120px;
  height: 120px;
  margin: 2vh auto;
  border-radius: 50%;
  box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.4);
  overflow: hidden;
  img {
    max-width: 100%;
  }
}

.memberContent {
  padding: 3vh 2vw;
  @include font(0.9rem, 300, 0px);
}

@media only screen and (max-width: 1024px) and (-webkit-min-device-pixel-ratio: 2) {
  .topArea {
    height: auto;
  }

  .textBox {
    padding: 6vh 6vw;
  }

  .topic {
    color: #847de0;
  }

  .imgBox {
    display: none;
  }

  .serCard,
  .techCard {
    width: 34vw;
    height: 40vh;
    margin-bottom: 5vh;
  }
}

@media screen and (max-width: 768px) and (-webkit-min-device-pixel-ratio: 2) {
  .serList,
  .textBox {
    display: block;
  }

  .textBox {
    .topic {
      @include font(3rem, 400, 0px);
    }
  }

  .serCard {
    width: 70vw;
    height: 25vh;
    margin: 0 auto 2vh auto;
  }

  .techBox {
    grid-template-rows: repeat(5, minmax(50px, 1fr));
    grid-template-areas:
      'neutral neutral neutral front front front'
      'neutral neutral neutral front front front'
      'neutral neutral neutral databases databases databases'
      'back back back sccs sccs sccs'
      'back back back ˙ ˙ ˙';
  }

  @media screen and (max-width: 500px) and (-webkit-min-device-pixel-ratio: 2) {
    .techBox {
      grid-template-columns: 1fr;
      grid-template-rows: repeat(9, minmax(50px, 1fr));
      grid-template-areas:
        'neutral'
        'neutral'
        'neutral'
        'front'
        'front'
        'back'
        'back'
        'sccs'
        'databases';
    }

    div[class*='techCard'] {
      padding: 0 4vw;
    }
  }
}
</style>
