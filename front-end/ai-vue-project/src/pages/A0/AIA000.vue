<template>
  <div>
    <Header />
    <div class="myContainer">
      <div class="sidebar">
        <div class="sidebarMenu">
          <a href="#" @click.prevent="status = 'dashboard'"
            ><li :class="{ sidebarColor: status === 'dashboard' }">
              Dashboard
            </li>
          </a>
          <a href="#" @click.prevent="status = 'table'"
            ><li :class="{ sidebarColor: status === 'table' }">Table</li>
          </a>
          <a href="#" @click.prevent="status = 'analysis'"
            ><li :class="{ sidebarColor: status === 'analysis' }">Analysis</li>
          </a>
        </div>
      </div>
      <div class="main">
        <div class="dashBoard" v-if="status === 'dashboard'">
          <div class="boardLeft">
            <div class="cardZone">
              <p class="cardTitle">Customer Information</p>
              <div class="myCard">
                <div class="cardImage">
                  <img src="@/assets/icon/faceScan.png" alt="" />
                </div>
                <div class="cardContent">
                  <p>來店時間 : {{ time }}</p>
                  <p>性別 : {{ gender }}</p>
                  <p>年齡 : {{ age }}</p>
                  <p>風格: {{ style }}</p>
                  <p>推薦商品: {{ recommandation }}</p>
                  <p></p>
                </div>
              </div>
            </div>
            <div class="cameraZone"></div>
          </div>

          <div class="boardMain">
            <p class="boardTopic">現在時間：{{ clock }}</p>
            <div class="boardFlow">
              <div class="timeCard">
                <div class="timeNow">
                  {{ time }}
                  <div class="line"></div>
                </div>
                <div class="timeCustomer">
                  <div class="customarCard">
                    <div class="profile">
                      <img src="@/assets/icon/faceScan.png" alt="" />
                    </div>
                    <div class="content">
                      <p>風格: {{ style }}</p>
                      <p>推薦商品：{{ recommandation }}</p>
                    </div>
                  </div>
                  <div class="customarCard"></div>
                  <div class="customarCard"></div>
                  <div class="customarCard"></div>
                  <div class="customarCard"></div>
                </div>
              </div>
              <div class="timeCard">
                <div class="timeNow">
                  {{ time }}
                  <div class="line"></div>
                </div>
                <div class="timeCustomer">
                  <div class="customarCard"></div>
                  <div class="customarCard"></div>
                  <div class="customarCard"></div>
                  <div class="customarCard"></div>
                </div>
              </div>
              <div class="timeCard">
                <div class="timeNow">
                  {{ time }}
                  <div class="line"></div>
                </div>
                <div class="timeCustomer">
                  <div class="customarCard"></div>
                  <div class="customarCard"></div>
                  <div class="customarCard"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="tableArea" v-if="status === 'table'">
          <table>
            <thead>
              <tr class="table__header table__row">
                <th class="table__cell table__cell--checkbox">
                  <input type="checkbox" />
                </th>
                <th class="table__cell table__cell--id">ID</th>
                <th class="table__cell table__cell--gender">性別</th>
                <th class="table__cell table__cell--age">年齡</th>
                <th class="table__cell table__cell--style">風格</th>
                <th class="table__cell table__cell--recommandation">
                  推薦商品
                </th>
                <th class="table__cell table__cell--time">來店時間</th>
              </tr>
            </thead>
            <tbody class="table__body">
              <tr class="table__row" v-for="n in 10" :key="n">
                <td class="table__cell table__cell--checkbox">
                  <input type="checkbox" />
                </td>
                <td class="table__cell table__cell--id">1</td>
                <td class="table__cell table__cell--gender">{{ gender }}</td>
                <td class="table__cell table__cell--age">{{ age }}</td>
                <td class="table__cell table__cell--style">{{ style }}</td>
                <td class="table__cell table__cell--recommandation">
                  {{ recommandation }}
                </td>
                <td class="table__cell table__cell--time">{{ time }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="analysis" v-if="status === 'analysis'">
          <div class="gender"><Bar /></div>
          <div class="age"><Bar2 /></div>
          <div class="color"><Pie /></div>
          <div class="style"><Pie2 /></div>
          <div class="style"><Profit /></div>
          <div class="style"><Worldcloud /></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from '@/components/F0/Header';
import Bar from '@/components/A0/Charts/Analyze_by_gneder';
import Bar2 from '@/components/A0/Charts/Analyze_by_age';
import Pie from '@/components/A0/Charts/Analyze_by_product';
import Pie2 from '@/components/A0/Charts/Analyze_by_color';
import Profit from '@/components/A0/Charts/Analyze_by_profit';
import Worldcloud from '@/components/A0/Charts/Analyze_by_cloud';

export default {
  name: 'AIA000',
  components: {
    Header,
    Bar,
    Bar2,
    Pie,
    Profit,
    Pie2,
    Worldcloud,
  },
  data() {
    return {
      status: 'dashboard',
      // customer info
      time: new Date().toLocaleTimeString(),
      gender: 'Ｆ',
      age: 25,
      style: 'fashion',
      recommandation: 'blue pants',
      timeInterval: null,
      clock: new Date().toLocaleTimeString().substring(10),
    };
  },
  created() {
    this.myClock();
  },
  mounted() {
    // eslint-disable-next-line no-console
    console.log(this.$store.state.accessToken);
    // eslint-disable-next-line no-console
    console.log(this.$store.state.user_name);
  },
  methods: {
    showToast() {
      this.$bvToast.toast(`歡迎回來${this.$route.params.user_name}`, {
        title: '登入訊息',
        variant: 'info',
        solid: true,
      });
    },
    myClock() {
      this.clock = new Date().toLocaleString().substring(10);
      this.timeInterval = setInterval(() => {
        const newClock = new Date();
        // const year = newClock.getFullYear();
        // const month = newClock.getMonth() + 1;
        // const date = newClock.getDate();
        // const time = newClock.toTimeString().substring(0, 8);
        const test = newClock.toLocaleString().substring(10);
        this.clock = test;
        // eslint-disable-next-line no-consol
      }, 1000);
    },
  },
};
</script>

<style scoped lang="scss">
p {
  margin: 0;
}

table {
  border: none;
  border-spacing: 0;
  border-collapse: collapse;
}
th,
td {
  text-align: initial;
}

.myContainer {
  width: 100vw;
  height: 100vh;
  display: flex;
  box-sizing: border-box;
  padding-top: 9vh;
}

//sidebar

.sidebar {
  width: 200px;
  padding: 1.2rem 0 1.5rem 1.2rem;
  background-color: #fefefe;
  .sidebarMenu {
    li {
      width: 100%;
      padding: 0.8rem;
      margin: 1rem 0;
      border-radius: 3px;
      color: rgb(175, 175, 175);
      &:hover {
        color: rgb(241, 241, 241);
        background-color: #7562df;
      }
    }
    .sidebarColor {
      color: rgb(241, 241, 241);
      background-color: #7562df;
    }
  }
}

// main

.main {
  flex: 1;
  margin: 1.2rem;
  background-color: #fafbff;
}

//Dashboard

.dashBoard {
  width: 100%;
  height: 100%;
  display: flex;
  border-radius: 3px;
  padding: 1rem;
  .boardLeft {
    width: 350px;
    display: flex;
    flex-direction: column;
    .cardZone {
      .cardTitle {
        padding-bottom: 1rem;
        font: {
          size: 1.5rem;
          weight: 300;
        }
        letter-spacing: 3px;
        text-align: center;
      }
      .myCard {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 1rem;
        border: none;
        border-radius: 1rem;
        background-color: #fefefe;
        box-shadow: 0 10px 30px -15px rgba(122, 104, 224, 0.4);
        .cardImage {
          width: 40%;
          text-align: center;
          img {
            max-width: 100%;
          }
        }
        .cardContent {
          padding-top: 1rem;
          p {
            font-weight: 300;
            letter-spacing: 0.1rem;
          }
        }
      }
    }
    .cameraZone {
      width: 100%;
      height: 200px;
      border: 1px solid black;
    }
  }
  .boardMain {
    flex: 1;
    display: flex;
    flex-direction: column;
    .boardTopic {
      padding-bottom: 1rem;
      font-size: 1.5rem;
      letter-spacing: 3px;
      text-align: center;
    }
    .boardFlow {
      height: 100%;
      margin-left: 1rem;
      padding: 1.2rem;
      overflow-y: auto;
      .timeCard {
        margin-bottom: 20px;
        .timeNow {
          position: relative;
          padding: 1rem 0;
          color: #7562df;
          font: {
            size: 1rem;
            weight: 300;
          }
          letter-spacing: 2px;
          .line {
            position: absolute;
            width: 100%;
            border: 0.3px solid #7562df;
          }
        }
        .timeCustomer {
          display: grid;
          grid-template-columns: repeat((auto-fit), minmax(200px, 1fr));
          grid-gap: 1rem;
          .customarCard {
            height: 80px;
            display: flex;
            justify-content: space-evenly;
            align-items: center;
            border-radius: 10px;
            background-color: #fefefe;
            box-shadow: 0 10px 30px -15px rgba(109, 94, 194, 0.4);
            .profile {
              width: 80px;
              img {
                max-width: 100%;
              }
            }
            .content {
              font-size: 0.8rem;
              letter-spacing: 1px;
            }
          }
        }
      }
    }
  }
}

//Table

.tableArea {
  width: 100%;
  height: 100%;
  padding: 2.5rem 2rem;
  display: flex;
  justify-content: center;
  .table__header {
    color: rgb(241, 241, 241);
    background-color: #7562df;
  }

  .table__body {
    background-color: #fefefe;
  }

  .table__row {
    height: 50px;
    max-height: 100px;
    border-bottom: 1px solid rgb(226, 226, 226);
  }

  .table__cell {
    text-align: center;
  }

  .table__cell--checkbox {
    width: 50px;
  }

  .table__cell--id {
    width: 80px;
  }

  .table__cell--gender {
    width: 80px;
  }

  .table__cell--age {
    width: 80px;
  }

  .table__cell--style {
    width: 80px;
  }

  .table__cell--recommandation {
    min-width: 200px;
  }

  .table__cell--time {
    min-width: 200px;
  }
}

//analysis

.analysis {
  height: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  .gender {
    background-color: #eee;
  }
  .age {
    background-color: #aaa;
  }
  .color {
    background-color: #aaa;
  }
  .style {
    background-color: #fff;
  }
}

@media screen and (max-width: 768px) and (-webkit-min-device-pixel-ratio: 2) {
}
</style>
