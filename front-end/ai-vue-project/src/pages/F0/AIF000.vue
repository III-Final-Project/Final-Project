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
        <p class="topic">hello</p>
        <p class="content">
          For the journal, see Machine Learning (journal). "Statistical
          learning" redirects here. For statistical learning in linguistics, see
          statistical learning in language acquisition.
        </p>
        <a class="topBtn" href="">Learn More</a>
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
      <div class="video-container">
        <!-- <iframe
          width="560"
          height="315"
          src="https://www.youtube.com/embed/r5J6e5_yyxI"
          title="YouTube video player"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
        ></iframe> -->
      </div>
    </div>
    <div class="spot" id="techView"></div>
    <div class="box tech">
      <p class="conTopic">技術一覽</p>
      <div class="techBox">
        <div class="techCard">
          <p>
            下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂
          </p>
          <p>隨時隨地聆聽。</p>
        </div>
        <div class="techCard">
          <p>
            下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂
          </p>
          <p>隨時隨地聆聽。</p>
        </div>
        <div class="techCard">
          <p>
            下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂
          </p>
          <p>隨時隨地聆聽。</p>
        </div>
        <div class="techCard">
          <p>
            下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂下載音樂
          </p>
          <p>隨時隨地聆聽。</p>
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
  data() {
    return {
      data: [
        { id: 1, username: 'Jyun' },
        { id: 2, username: 'Michael' },
      ],
    };
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
  padding: 8vh 4vw;
}

.topic {
  font-size: 5rem;
  letter-spacing: 2px;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  padding: 20px 0;
}

.content {
  padding: 20px 15px;
  line-height: 1.25em;
}

.imgBox {
  flex: 1;
  background-image: url('~@/assets/img/page-mainpic.png');
  background-repeat: no-repeat;
  background-position: center;
  background-size: 85%;
}

.topBtn {
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  font-size: 16px;
  box-sizing: border-box;
  padding: 8px 25px 8px 25px;
  margin: 0 30px;
  float: right;
  color: #f75c2f;
  border: #f75c2f 3px solid;
  border-radius: 60px;
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
  font-size: 2.875rem;
  text-align: center;
}

.vission {
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
  padding: 0 10vw;
}

.serCard {
  flex: 1;
  height: 65vh;
  background-color: #cd9df1;
  box-shadow: 1px 1px 5px 2px rgba(139, 138, 139, 0.3);
  margin: 0 2vw;
}

.features .conTopic,
.tech .conTopic {
  color: rgb(95, 94, 94);
}

.demo {
  background-color: rgb(46, 45, 45);
  .myVideo {
    text-align: center;
  }
}

.techBox {
  display: flex;
}

.techCard {
  flex: 1;
  height: 40vh;
  background-color: rgba(250, 225, 225, 0.75);
  margin: 0 2vw;
}

.video-container {
  position: relative;
  padding-bottom: 56.25%;
  padding-top: 30px;
  height: 0;
  overflow: hidden;
}

.video-container iframe,
.video-container object,
.video-container embed {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

@media only screen and (min-device-width: 375px) and (max-device-width: 1024px) and (-webkit-min-device-pixel-ratio: 2) {
  .topArea {
    height: auto;
  }

  .textBox {
    padding: 6vh 4vw;
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

  .serList {
    display: block;
  }

  .serCard {
    height: 50vh;
    margin-bottom: 5vh;
  }

  .tech .techBox {
    display: block;
  }

  .techCard {
    margin-bottom: 2vh;
  }
}
</style>
