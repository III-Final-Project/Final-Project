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
          <a href="#" @click.prevent="status = 'camera'"
            ><li :class="{ sidebarColor: status === 'camera' }">Camera</li>
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
                  <img :src="profileUrl" alt="" />
                </div>
                <div class="cardContent">
                  <p>來店時間 : {{ time | filterTime }}</p>
                  <p>性別 : {{ gender }}</p>
                  <p>年齡 : {{ age }}</p>
                  <p>喜好顏色: {{ style }}</p>
                  <p>推薦商品: {{ recommandation }}</p>
                  <p></p>
                </div>
                <div class="cardRecommendImg">
                  <img :src="imgUrl" alt="" />
                </div>
              </div>
            </div>
          </div>
          <div class="boardMain">
            <div class="boardTop">
              <p class="boardTopic">現在時間：{{ clock }}</p>
              <div class="btnArea">
                <button
                  class="btns"
                  :class="{ purple: active }"
                  @click="active = true"
                >
                  啟動偵測
                </button>
                <button
                  class="btns"
                  :class="{ purple: !active }"
                  @click="active = false"
                >
                  關閉偵測
                </button>
              </div>
            </div>
            <div class="boardFlow">
              <div class="timeCard">
                <select id="timer" @change="changeTime">
                  <option disabled selected>選擇時間</option>
                  <option value="全部資料">全部資料</option>
                  <option
                    v-for="(item, index) in timeRange"
                    :value="item.val"
                    :key="index"
                  >
                    {{ item.time }}
                  </option>
                </select>
                <div class="timeNow">
                  {{ selectedTime }}&nbsp;&nbsp;共{{ totalUsers }}筆資料
                  <div class="line"></div>
                  <!-- pagination -->
                  <nav class="navigation">
                    <ul class="pagination">
                      <li v-for="i in totalPages" :key="i">
                        <a
                          class="page-link"
                          href="#"
                          @click.prevent="selectedPage = i"
                          >{{ i }}</a
                        >
                      </li>
                    </ul>
                  </nav>
                </div>
                <div class="timeCustomer">
                  <div
                    class="customerCard"
                    :class="{ showPurple: cardNumber === item.id }"
                    v-for="(item, index) in getUsersByPage"
                    :key="index"
                    @click="changeCard(item, index)"
                  >
                    <div class="profile">
                      <img :src="baseUrl + item.customer_img_path" alt="" />
                    </div>
                    <div class="content">
                      <p>來店時間：{{ item.customer_time }}</p>
                      <p>推薦商品：{{ item.customer_sex }}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="tableArea" v-if="status === 'table'">
          <table>
            <thead>
              <tr class="table__header table__row">
                <th class="table__cell table__cell--id">ID</th>
                <th class="table__cell table__cell--gender">性別</th>
                <th class="table__cell table__cell--age">年齡</th>
                <th class="table__cell table__cell--style">喜好顏色</th>
                <th class="table__cell table__cell--recommandation">
                  推薦商品
                </th>
                <th class="table__cell table__cell--time">來店時間</th>
                <th class="table__cell table__cell--delete">DELETE ALL</th>
              </tr>
            </thead>
            <tbody class="table__body">
              <tr class="table__row" v-for="item in details" :key="item.id">
                <td class="table__cell table__cell--id">{{ item.id }}</td>
                <td class="table__cell table__cell--gender">
                  {{ item.customer_sex }}
                </td>
                <td class="table__cell table__cell--age">
                  {{ item.customer_age }}
                </td>
                <td class="table__cell table__cell--style">{{ style }}</td>
                <td class="table__cell table__cell--recommandation">
                  {{ recommandation }}
                </td>
                <td class="table__cell table__cell--time">
                  {{ item.customer_time }}
                </td>
                <td class="table__cell table__cell--delete">DELETE</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="analysis" v-if="status === 'analysis'">
          <div class="gender"><Bar /></div>
          <div class="age"><Bar2 /></div>
          <div class="color"><Pie /></div>
          <div class="style"><Pie2 /></div>
          <!-- <div class="style"><Profit /></div> -->
          <div class="style"><Worldcloud /></div>
        </div>
        <div class="camera" v-if="status === 'camera'">
          <div class="btnArea">
            <button
              class="btns"
              :class="{ purple: active }"
              @click="active = true"
            >
              啟動偵測
            </button>
            <button
              class="btns"
              :class="{ purple: !active }"
              @click="active = false"
            >
              關閉偵測
            </button>
          </div>
          <div class="cameraArea"></div>
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
// import Face from '../../service/face';

const res = {
  returnCode: '200',
  detail: [
    {
      id: '1',
      user_name: 'jyun',
      customer_sex: 'female',
      customer_age: '25',
      customer_time: '2021-6-6 12:4:43',
      customer_img_path: 'static/image/jyun121212.jpg',
      customer_recommend_img:
        'data:image/jpeg;base64,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',
    },
    {
      id: '2',
      user_name: 'jyun',
      customer_sex: 'female',
      customer_age: '20',
      customer_time: '2021-6-6 12:4:43',
      customer_img_path: 'static/image/customer/2021-6-6 17:4:43',
      customer_recommend_img:
        'data:image/jpeg;base64,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',
    },
    {
      id: '3',
      user_name: 'jyun',
      customer_sex: 'male',
      customer_age: '25',
      customer_time: '2021-6-6 13:4:43',
      customer_img_path: 'static/image/customer/2021-6-6 17:4:43',
      customer_recommend_img:
        'data:image/jpeg;base64,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',
    },
    {
      id: '4',
      user_name: 'jyun',
      customer_sex: 'male',
      customer_age: '30',
      customer_time: '2021-6-6 13:4:43',
      customer_img_path: 'static/image/customer/2021-6-6 17:4:43',
      customer_recommend_img:
        'data:image/jpeg;base64,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',
    },
    {
      id: '5',
      user_name: 'jyun',
      customer_sex: 'female',
      customer_age: '15',
      customer_time: '2021-6-6 17:4:43',
      customer_img_path: 'static/image/customer/2021-6-6 17:4:43',
      customer_recommend_img:
        'data:image/jpeg;base64,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',
    },
    {
      id: '6',
      user_name: 'jyun',
      customer_sex: 'male',
      customer_age: '18',
      customer_time: '2021-6-6 17:4:43',
      customer_img_path: 'static/image/customer/2021-6-6 17:4:43',
      customer_recommend_img:
        'data:image/jpeg;base64,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',
    },
  ],
};
export default {
  filters: {
    filterTime(value) {
      return value.substring(9);
    },
  },
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
      active: false,
      // customer info
      time: '',
      gender: '',
      age: '',
      style: '',
      recommandation: '',
      profileUrl: '../../../static/user.png',
      imgUrl: '../../../static/customer-reminder.png',
      baseUrl: '../../../../../python/FlaskServer/',
      // clock
      timeInterval: null,
      clock: new Date().toLocaleTimeString().substring(9),
      // pagination
      users_per_page: 8,
      selectedPage: 1,
      // data
      details: [],
      cacheDatas: [],
      cardNumber: 0,
      // time selecting
      timeRange: [
        { time: '11:00 - 12:00', val: '11:00 - 12:00' },
        { time: '12:00 - 13:00', val: '12:00 - 13:00' },
        { time: '13:00 - 14:00', val: '13:00 - 14:00' },
        { time: '14:00 - 15:00', val: '14:00 - 15:00' },
        { time: '15:00 - 16:00', val: '15:00 - 16:00' },
        { time: '16:00 - 17:00', val: '16:00 - 17:00' },
        { time: '17:00 - 18:00', val: '17:00 - 18:00' },
        { time: '18:00 - 19:00', val: '18:00 - 19:00' },
        { time: '19:00 - 20:00', val: '19:00 - 20:00' },
      ],
      selectedTime: '',
    };
  },
  created() {
    this.myClock();
    this.fetchData();
  },
  mounted() {
    if (Object.keys(this.$route.params).length !== 0) {
      this.showToast();
    }
    const userName = this.$route.params.user_name;
    this.axios.post('http://127.0.0.1:5000/api/customer/fashion', {
      user_name: userName,
    });
    // .then((res) => {
    //   // eslint-disable-next-line no-console
    //   console.log(res.data);
    // });
  },
  methods: {
    fetchData() {
      if (res.returnCode === '200') {
        this.details = res.detail;
        this.cacheDatas = this.details;
      }
    },
    showToast() {
      this.$bvToast.toast(`歡迎回來 ${this.$route.params.user_name}`, {
        title: '登入訊息',
        variant: 'info',
        solid: true,
      });
    },
    myClock() {
      this.clock = new Date().toLocaleString().substring(9);
      this.timeInterval = setInterval(() => {
        const newClock = new Date();
        // const year = newClock.getFullYear();
        // const month = newClock.getMonth() + 1;
        // const date = newClock.getDate();
        // const time = newClock.toTimeString().substring(0, 8);
        const test = newClock.toLocaleString().substring(9);
        this.clock = test;
      }, 1000);
    },
    changeTime() {
      const time = document.querySelector('#timer');
      this.selectedTime = time.value;
      if (this.selectedTime === '全部資料') {
        this.cacheDatas = this.details;
      } else {
        const timeStart = `${this.selectedTime.substring(0, 2)}`;
        const timeEnd = `${this.selectedTime.substring(8, 10)}`;
        this.cacheDatas = [];
        this.details.forEach((element) => {
          const enterTime = element.customer_time.substring(9, 11);
          if (enterTime === timeStart && enterTime < timeEnd) {
            this.cacheDatas.push(element);
          }
        });
      }
    },
    changeCard(item) {
      this.cardNumber = item.id;
      // const customerTime =
      //   item.time.substring(0, 2) + item.time.substring(3, 5);
      // if (customerTime < 1200) {
      //   this.time = `上午${item.time}`;
      // } else {
      //   this.time = `下午${item.time}`;
      // }
      this.time = item.customer_time;
      this.gender = item.customer_sex;
      this.age = item.customer_age;
      this.style = item.style;
      this.recommandation = item.recommandation;
      this.imgUrl = item.customer_recommend_img;
    },
  },
  computed: {
    totalUsers() {
      return this.cacheDatas.length;
    },
    totalPages() {
      return Math.ceil(this.totalUsers / this.users_per_page);
    },
    getUsersByPage() {
      // 計算起始index
      const startIndex = (this.selectedPage - 1) * this.users_per_page;
      return this.cacheDatas.slice(
        startIndex,
        startIndex + this.users_per_page,
      );
    },
  },
  watch: {
    selectedTime() {
      this.selectedPage = 1;
    },
  },
};
</script>

<style scoped lang="scss">
$main_color: #c180d3;
$side_color: #fafbff;

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

//btns

.btnArea {
  position: absolute;
  display: inline-block;
  top: 0;
  right: 0;
  .purple {
    color: white;
    background-color: $main_color;
  }
}
.btns {
  display: inline-block;
  padding: 5px 10px;
  margin-left: 1rem;
  border: 1px solid #d2d6da;
  border-radius: 0.5rem;
  background-color: $side_color;
  outline: none;
  &:hover {
    color: white;
    background-color: $main_color;
  }
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
        background-color: $main_color;
      }
    }
    .sidebarColor {
      color: rgb(241, 241, 241);
      background-color: $main_color;
    }
  }
}

// main

.main {
  flex: 1;
  margin: 1.2rem;
}

//Dashboard

.dashBoard {
  width: 100%;
  height: 100%;
  display: flex;
  border-radius: 3px;
  padding: 1rem;
  background-color: $side_color;
  .boardLeft {
    display: flex;
    flex-direction: column;
    padding: 1rem;
    overflow-y: auto;
    .cardZone {
      .cardTitle {
        padding-bottom: 1rem;
        font: {
          size: 1.3rem;
          weight: 300;
        }
        letter-spacing: 3px;
        text-align: center;
      }
      .myCard {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 0 auto;
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
          width: 168px;
          padding: 1rem 0;
          p {
            font: {
              size: 0.9rem;
              weight: 300;
            }
            letter-spacing: 0.1rem;
          }
        }
        .cardRecommendImg {
          max-width: 210px;
          height: 210px;
          img {
            max-width: 100%;
            max-height: 100%;
            margin: 0 auto;
          }
        }
      }
    }
  }
  .boardMain {
    flex: 1;
    display: flex;
    flex-direction: column;
    margin-left: 1rem;
    padding: 1rem;
    .boardTop {
      position: relative;
    }
    .boardTopic {
      display: inline-block;
      padding-bottom: 1rem;
      font-size: 1.5rem;
      letter-spacing: 3px;
      text-align: center;
    }
    .boardFlow {
      height: 100%;
      overflow-y: auto;
      .timeCard {
        margin-bottom: 20px;
        .timeNow {
          position: relative;
          padding: 1rem 0;
          color: $main_color;
          font: {
            size: 1rem;
            weight: 300;
          }
          letter-spacing: 2px;
          .line {
            position: absolute;
            width: 100%;
            border: 0.3px solid $main_color;
          }
          .navigation {
            position: absolute;
            top: 0;
            right: 0;
          }
        }
        .timeCustomer {
          display: grid;
          grid-template-columns: repeat((auto-fit), minmax(240px, 1fr));
          grid-gap: 1rem 1.5rem;
          .customerCard {
            position: relative;
            height: 80px;
            border-radius: 10px;
            background-color: #fefefe;
            box-shadow: 0 10px 10px -15px rgba(109, 94, 194, 0.4);
            cursor: pointer;
            .profile {
              width: 80px;
              img {
                max-width: 100%;
              }
            }
            .content {
              position: absolute;
              top: 25%;
              left: 120px;
              font-size: 0.8rem;
              letter-spacing: 1px;
            }
          }
          .showPurple {
            background: linear-gradient(to left, #fdeaea, rgb(255, 255, 255));
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
  background-color: $side_color;
  .table__header {
    color: rgb(241, 241, 241);
    background-color: $main_color;
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
    min-width: 180px;
  }

  .table__cell--time {
    min-width: 180px;
  }

  .table__cell--delete {
    min-width: 150px;
  }
}

//analysis

.analysis {
  height: 100%;

  .gender,
  .age,
  .color,
  .style {
    padding: 2rem 0;
    background-color: $side_color;
    border-bottom: 0.5px rgb(199, 199, 199) solid;
  }
}

//camera

.camera {
  position: relative;
  width: 100%;
  height: 100%;
  background-color: $side_color;
  .cameraArea {
    width: 100%;
    height: 100%;
  }
}

//navigation

.navigation {
  .page-link {
    color: $main_color;
  }
}

@media screen and (max-width: 768px) and (-webkit-min-device-pixel-ratio: 2) {
}
</style>
