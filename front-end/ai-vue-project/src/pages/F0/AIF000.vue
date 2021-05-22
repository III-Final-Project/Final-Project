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
        <p class="content">
          For the journal, see Machine Learning (journal). "Statistical
          learning" redirects here. For statistical learning in linguistics, see
          statistical learning in language acquisition.
        </p>
        <a class="topBtn" href="#demo">Learn More</a>
      </div>
      <div class="imgBox"></div>
    </div>
    <div class="spot" id="vission"></div>
    <div class="box vission">
      <p class="conTopic">使用理念</p>
      <div class="viContentBox">
        <!-- <div class="viImg"></div> -->
        <div class="viText">
          <p class="content">
            For the journal, see Machine Learning (journal). "Statistical
            learning" redirects here. For statistical learning in linguistics,
            see statistical learning in language acquisition.
          </p>
        </div>
      </div>
    </div>
    <div class="spot" id="service"></div>
    <div class="box features">
      <p class="conTopic">服務項目</p>
      <div class="serList">
        <div class="serCard">
          <p>
            下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂
          </p>
          <p>隨時隨地聆聽。</p>
        </div>
        <div class="serCard">
          <p>無廣告打擾。</p>
          <p>享受不間斷的音樂。</p>
        </div>
        <div class="serCard">
          <p>愛聽什麼、就播什麼。</p>
          <p>行動裝置照樣聽。</p>
        </div>
        <div class="serCard">
          <p>愛聽什麼、就播什麼。</p>
          <p>行動裝置照樣聽。</p>
        </div>
      </div>
    </div>
    <div class="spot" id="demo"></div>
    <div class="demo">
      <p class="conTopic">成果展示</p>
    </div>
    <div class="spot" id="tech"></div>
    <div class="box techArea">
      <p class="conTopic">技術一覽</p>
      <div class="techBox">
        <div class="techCard-1">
          <div class="techBanner">
            <div class="techIcon"></div>
            <div class="techTitle">Neutral Networks</div>
          </div>
          <div class="techContent">
            <p class="subTitle">FrameWork</p>
            <p>- Flask</p>
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
            <p class="subTitle">Face Recognition Service</p>
            <p>- Azure</p>
            <p>- Face Recognition Model</p>
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
            <p class="subTitle">Tools</p>
            <p>- Webpack</p>
            <p>- Webcam</p>
            <p>- Bootstrap</p>
          </div>
          <div class="techContent">
            <p class="subTitle">UI & UX</p>
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
          </div>
          <div class="techContent">
            <p class="subTitle">Tools</p>
            <p>- RESTful API</p>
            <p>- JWT</p>
            <p>- Email & SMS Server</p>
            <p>- Login with Access right system</p>
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
            <p>- Coding Style | Airbnb</p>
          </div>
        </div>
      </div>
    </div>
    <!-- 開發人員 -->
    <div class="spot" id="member"></div>
    <div class="memberArea">
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
            <!-- <p class="memberContent">前端開發<br />UI & UX</p> -->
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
};
</script>

<style scoped lang="scss">
p {
  margin: 0;
}

.spot {
  position: relative;
  top: -8vh;
  display: block;
  visibility: hidden;
}

.main {
  padding-top: 13vh;
}

.topArea {
  display: flex;
  height: 87vh;
}

.textBox {
  flex: 1;
  padding: 8vh 5vw;
}

.topic {
  padding: 20px 0;
  font-size: 3em;
  letter-spacing: 3px;
}

.content {
  padding: 20px 0;
  line-height: 1.25em;
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

.topBtn {
  float: right;
  box-sizing: border-box;
  padding: 8px 25px 8px 25px;
  margin: 0 30px;
  border: #f75c2f 3px solid;
  border-radius: 60px;
  color: #f75c2f;
  font-size: 16px;
  transition: 0.35s;
  &:hover {
    background: linear-gradient(#e06f6f, #f75c2f);
    color: white;
  }
}

.box {
  padding-left: 2vw;
  padding-right: 2vw;
  padding-bottom: 8vh;
}

.conTopic {
  color: white;
  padding: 5vh 0;
  letter-spacing: 2px;
  font-size: 2.2rem;
  text-align: center;
}

.vission {
  margin: 20px 6vw;
  border-radius: 50px;
  background-color: rgb(66, 66, 80);
}

.viContentBox .viText {
  padding: 0 2vw;
  .topic {
    color: beige;
  }
  .content {
    color: beige;
  }
}

.serList {
  display: flex;
  flex-wrap: wrap;
  padding: 0 10vw;
}

.serCard {
  width: 15vw;
  height: 65vh;
  background-color: #cd9df1;
  box-shadow: 1px 1px 5px 2px rgba(139, 138, 139, 0.3);
  margin: 0 2vw;
}
.memberArea .conTopic,
.features .conTopic,
.techArea .conTopic {
  color: rgb(95, 94, 94);
}

.demo {
  margin: 20px 6vw;
  border-radius: 50px;
  background-color: rgb(46, 45, 45);
  .myVideo {
    text-align: center;
  }
}

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
  padding: 0 4vw;
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

div[class*='techCard'] {
  padding: 0 2vw;
  border-radius: 15px;
  background-color: rgb(245, 245, 245);
  overflow: hidden;
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
    padding-left: 2vw;
    font: {
      size: 1.5em;
      weight: bold;
    }
  }
}

.techContent {
  padding: 2vh 0;
  .subTitle {
    padding-bottom: 1vh;
    color: #a82973;
    font-size: 18px;
  }
}

// member

.memberBox {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  grid-gap: 1.5rem;
  padding: 0 6vw;
  padding-bottom: 8vh;
}

.memberCard {
  min-height: 250px;
  border-radius: 20px;
  background-color: rgb(245, 245, 245);
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
  font: {
    weight: bold;
  }
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

  .viContentBox {
    height: auto;
  }

  .viContentBox .viText {
    padding: 0 4vw;
  }

  .viImg {
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

  .serCard {
    width: 70vw;
    height: 25vh;
    margin: 0 auto 2vh auto;
  }

  .techBox {
    grid-template-areas:
      'neutral neutral neutral front back'
      'neutral neutral neutral front back'
      'neutral databases sccs';
  }
}
</style>
