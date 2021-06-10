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
          <a href="#" @click.prevent="status = 'camera'"
            ><li :class="{ sidebarColor: status === 'camera' }">Camera</li>
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
                  <img :src="customerImg" alt="" />
                </div>
                <div class="cardContent">
                  <p>來店時間 : {{ time }}</p>
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
                  @click="startCamera"
                >
                  啟動偵測
                </button>
                <button
                  class="btns"
                  :class="{ purple: !active }"
                  @click="stopCamera"
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
                      <img :src="item.customer_img_path" />
                    </div>
                    <div class="content">
                      <p>
                        來店時間: {{ item.customer_time.substring(11, 16) }}
                      </p>
                      <p>推薦商品：{{ item.customer_recommend_product }}</p>
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
              <tr
                class="table__row"
                v-for="(item, index) in details"
                :key="item.id"
              >
                <td class="table__cell table__cell--id">{{ index }}</td>
                <td class="table__cell table__cell--gender">
                  {{ item.customer_sex }}
                </td>
                <td class="table__cell table__cell--age">
                  {{ item.customer_age }}
                </td>
                <td class="table__cell table__cell--style">{{ style }}</td>
                <td class="table__cell table__cell--recommandation">
                  {{ item.customer_recommend_product }}
                </td>
                <td class="table__cell table__cell--time">
                  {{ item.customer_time }}
                </td>
                <td class="table__cell table__cell--delete">
                  <button @click="deleteData(item.id)">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="analysis" v-if="status === 'analysis'">
          <div class="gender"><Bar :myData="details" /></div>
          <div class="age"><Bar2 :myData="details" /></div>
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
              @click="startCamera"
            >
              啟動偵測
            </button>
            <button
              class="btns"
              :class="{ purple: !active }"
              @click="stopCamera"
            >
              關閉偵測
            </button>
          </div>
          <div class="cameraArea">
            <img :src="myCamera" />
          </div>
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
      active: false,
      // customer info
      imgUrl: '../../../static/customer-reminder.png',
      time: '',
      gender: 'Ｆ',
      age: 25,
      style: 'fashion',
      recommandation: 'blue pants',
      customerImg: '../../../static/user.png',
      myCamera: null,
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
    this.queryCustomerData();
  },
  mounted() {
    if (Object.keys(this.$route.params).length !== 0) {
      this.showToast();
    }
    // const userName = this.$route.params.user_name;
    // this.axios.post('http://127.0.0.1:5000/api/customer/fashion', {
    //   user_name: userName,
    // });
    // .then((res) => {
    //   // eslint-disable-next-line no-console
    //   console.log(res.data);
    // });
  },
  methods: {
    queryCustomerData() {
      this.axios
        .get(
          `http://127.0.0.1:5000/api/customer/query/${this.$store.state.user_name}`,
        )
        .then((res) => {
          if (res.data.returnCode === '200') {
            const basicCustomerImgPath = 'http://127.0.0.1:5000/';
            res.data.detail.forEach((item) => {
              const customerObj = {
                id: item.id,
                customer_sex: item.customer_sex,
                customer_age: item.customer_age,
                customer_time: item.customer_time,
                // customer_img_path: basic_customer_img_path + item.customer_img_path,
                customer_img_path: `${basicCustomerImgPath}static/image/customer/customer2021-6-6 17:8:15.jpg`,
                customer_recommend_product: item.customer_recommend_product,
                customer_recommend_color: item.customer_recommend_color,
                customer_recommend_img: item.customer_recommend_img,
              };
              this.details.push(customerObj);
            });
            this.cacheDatas = this.details;
          }
        });
    },
    deleteData(id) {
      this.axios
        .delete(`http://localhost:5000//api/customer/${id}`)
        .then((res) => {
          if (res.data.returnCode === '200') {
            this.$bvToast.toast(`刪除成功`, {
              title: '刪除訊息',
              variant: 'success',
              solid: true,
            });
            this.details = [];
            this.queryCustomerData();
          }
        });
    },
    startCamera() {
      // eslint-disable-next-line no-console
      console.log('start camera');
      this.myCamera = 'http://localhost:5000/api/customer/fashion';
      this.active = true;
    },
    stopCamera() {
      // eslint-disable-next-line no-console
      console.log('stop camera');
      this.axios.delete('http://localhost:5000/api/customer/fashion');
      this.myCamera = null;
      this.active = false;
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
          const enterTime = element.customer_time.substring(11, 13);
          if (enterTime === timeStart && enterTime < timeEnd) {
            this.cacheDatas.push(element);
          }
        });
      }
    },
    changeCard(item) {
      const customerTime =
        item.customer_time.substring(11, 13) +
        item.customer_time.substring(14, 16);
      if (customerTime < 1200) {
        this.time = `上午${item.customer_time.substring(11, 16)}`;
      } else if (customerTime < 1300) {
        this.time = `下午${item.customer_time.substring(11, 16)}`;
      } else {
        this.time = `下午${
          item.customer_time.substring(11, 13) - 12
        }:${item.customer_time.substring(14, 16)}`;
      }
      this.cardNumber = item.id;
      this.gender = item.customer_sex;
      this.age = item.customer_age;
      this.customerImg = item.customer_img_path;
      this.style = item.customer_recommend_color;
      this.recommandation = item.customer_recommend_product;
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
