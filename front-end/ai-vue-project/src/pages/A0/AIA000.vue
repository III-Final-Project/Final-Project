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
                <div class="cardRecommendImg">
                  <img :src="imgUrl" alt="" />
                </div>
              </div>
            </div>
          </div>

          <div class="boardMain">
            <p class="boardTopic">現在時間：{{ clock }}</p>
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
                    class="customarCard"
                    v-for="(item, index) in getUsersByPage"
                    :key="index"
                    @click="changeCard(item)"
                  >
                    <div class="profile">
                      <img src="@/assets/icon/faceScan.png" alt="" />
                    </div>
                    <div class="content">
                      <p>來店時間: {{ item.time }}</p>
                      <p>推薦商品：{{ item.recommandation }}</p>
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
              <tr class="table__row" v-for="n in 8" :key="n">
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
      imgUrl: 'https://0.0.0.0:8080/static/img/clothing.909cfb6.jpeg',
      // clock
      timeInterval: null,
      clock: new Date().toLocaleTimeString().substring(9),
      // pagination
      users_per_page: 8,
      selectedPage: 1,
      // data
      details: [
        {
          time: '13:05',
          gender: 'M',
          age: 20,
          style: 'street',
          recommandation: 'white pants',
          imgUrl:
            'https://img.mytheresa.com/1088/1088/66/jpeg/catalog/product/bb/P00524623.jpg',
        },
        {
          time: '11:30',
          gender: 'M',
          age: 20,
          style: 'street',
          recommandation: 'white pants',
          imgUrl:
            'https://img.mytheresa.com/1088/1088/66/jpeg/catalog/product/bb/P00524623.jpg',
        },
        {
          time: '15:21',
          gender: 'F',
          age: 21,
          style: 'casual',
          recommandation: 'overall',
          imgUrl:
            'https://cdn0-manfashion.techbang.com/system/images/63244/medium/c45fc441fbb69dc85ca5b4825ee6e04c.jpg?1503301567',
        },
        {
          time: '15:40',
          gender: 'F',
          age: 21,
          style: 'casual',
          recommandation: 'overall',
          imgUrl:
            'https://cdn0-manfashion.techbang.com/system/images/63244/medium/c45fc441fbb69dc85ca5b4825ee6e04c.jpg?1503301567',
        },
        {
          time: '10:59',
          gender: 'M',
          age: 21,
          style: 'casual',
          recommandation: 'coats',
          imgUrl:
            'https://cdn-images.farfetch-contents.com/15/91/54/16/15915416_29453221_480.jpg',
        },
        {
          time: '17:59',
          gender: 'F',
          age: 21,
          style: 'casual',
          recommandation: 'overall',
          imgUrl:
            'https://cdn-images.farfetch-contents.com/15/91/54/16/15915416_29453221_480.jpg',
        },
        {
          time: '15:10',
          gender: 'M',
          age: 21,
          style: 'casual',
          recommandation: 'pants',
          imgUrl:
            'https://img.mytheresa.com/1088/1088/66/jpeg/catalog/product/bb/P00524623.jpg',
        },
        {
          time: '18:25',
          gender: 'F',
          age: 66,
          style: 'casual',
          recommandation: 'dress',
          imgUrl:
            'http://cdn.shopify.com/s/files/1/0932/1794/products/HHH061_NesliNapDress_LightBlueGlitterCheck_A_grande.jpg?v=1612806814',
        },
        {
          time: '19:25',
          gender: 'F',
          age: 42,
          style: 'fashion',
          recommandation: 'overall',
          imgUrl:
            'https://img.mytheresa.com/1088/1088/66/jpeg/catalog/product/bb/P00524623.jpg',
        },

        {
          time: '19:34',
          gender: 'M',
          age: 58,
          style: 'casual',
          recommandation: 'overall',
          imgUrl:
            'https://img.mytheresa.com/1088/1088/66/jpeg/catalog/product/bb/P00524623.jpg',
        },
        {
          time: '17:32',
          gender: 'F',
          age: 21,
          style: 'formal',
          recommandation: 'overall',
          imgUrl:
            'https://rexformalwear.com/wp-content/uploads/2020/12/Rex-75th-Anniversary-Black-Notch-Tuxedo.jpg',
        },
        {
          time: '12:50',
          gender: 'F',
          age: 35,
          style: 'casual',
          recommandation: 'glasses',
          imgUrl:
            'https://img.mytheresa.com/1088/1088/66/jpeg/catalog/product/bb/P00524623.jpg',
        },
        {
          time: '19:35',
          gender: 'F',
          age: 42,
          style: 'fashion',
          recommandation: 'overall',
          imgUrl:
            'https://img.mytheresa.com/1088/1088/66/jpeg/catalog/product/bb/P00524623.jpg',
        },

        {
          time: '17:40',
          gender: 'M',
          age: 58,
          style: 'casual',
          recommandation: 'overall',
          imgUrl:
            'https://cdn.shopify.com/s/files/1/0120/0311/5089/articles/blue-blazer2_800x.jpg?v=1604464651',
        },
        {
          time: '13:40',
          gender: 'F',
          age: 35,
          style: 'casual',
          recommandation: 'glasses',
          imgUrl:
            'https://static.dezeen.com/uploads/2020/02/harikrishnan-lcf-latex-fashion-design_dezeen_2364_sq2.jpg',
        },
        {
          time: '14:08',
          gender: 'F',
          age: 42,
          style: 'fashion',
          recommandation: 'overall',
          imgUrl:
            'https://static.dezeen.com/uploads/2020/02/harikrishnan-lcf-latex-fashion-design_dezeen_2364_sq2.jpg',
        },

        {
          time: '14:30',
          gender: 'M',
          age: 58,
          style: 'casual',
          recommandation: 'overall',
          imgUrl:
            'https://static.dezeen.com/uploads/2020/02/harikrishnan-lcf-latex-fashion-design_dezeen_2364_sq2.jpg',
        },
        {
          time: '18:23',
          gender: 'F',
          age: 35,
          style: 'casual',
          recommandation: 'glasses',
          imgUrl:
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3GbXdID0E0D7Dxbe9Waeel4E-Ler8BPcjFQ&usqp=CAU',
        },
        {
          time: '14:39',
          gender: 'F',
          age: 42,
          style: 'fashion',
          recommandation: 'overall',
          imgUrl:
            'https://cdn1-manfashion.techbang.com/system/images/63247/medium/c71316cdd0e817fe682f883602bc9a2f.jpg?1503301569',
        },
        {
          time: '11:40',
          gender: 'M',
          age: 58,
          style: 'casual',
          recommandation: 'overall',
          imgUrl:
            'https://cdn1-manfashion.techbang.com/system/images/63247/medium/c71316cdd0e817fe682f883602bc9a2f.jpg?1503301569',
        },
        {
          time: '11:40',
          gender: 'M',
          age: 58,
          style: 'casual',
          recommandation: 'overall',
          imgUrl:
            'https://cdn1-manfashion.techbang.com/system/images/63247/medium/c71316cdd0e817fe682f883602bc9a2f.jpg?1503301569',
        },
        {
          time: '11:40',
          gender: 'M',
          age: 58,
          style: 'casual',
          recommandation: 'overall',
          imgUrl:
            'https://cdn1-manfashion.techbang.com/system/images/63247/medium/c71316cdd0e817fe682f883602bc9a2f.jpg?1503301569',
        },
        {
          time: '11:40',
          gender: 'M',
          age: 58,
          style: 'casual',
          recommandation: 'overall',
          imgUrl:
            'https://cdn1-manfashion.techbang.com/system/images/63247/medium/c71316cdd0e817fe682f883602bc9a2f.jpg?1503301569',
        },
        {
          time: '11:40',
          gender: 'M',
          age: 58,
          style: 'casual',
          recommandation: 'overall',
          imgUrl:
            'https://cdn1-manfashion.techbang.com/system/images/63247/medium/c71316cdd0e817fe682f883602bc9a2f.jpg?1503301569',
        },
        {
          time: '11:40',
          gender: 'M',
          age: 58,
          style: 'casual',
          recommandation: 'overall',
          imgUrl:
            'https://cdn1-manfashion.techbang.com/system/images/63247/medium/c71316cdd0e817fe682f883602bc9a2f.jpg?1503301569',
        },
        {
          time: '11:40',
          gender: 'M',
          age: 58,
          style: 'casual',
          recommandation: 'overall',
          imgUrl:
            'https://img.mytheresa.com/1088/1088/66/jpeg/catalog/product/bb/P00524623.jpg',
        },
      ],
      cacheDetals: [],
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
    this.cacheDetals = this.details;
  },
  mounted() {
    if (Object.keys(this.$route.params).length !== 0) {
      this.showToast();
    }
  },
  methods: {
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
        // eslint-disable-next-line no-consol
      }, 1000);
    },
    changeTime() {
      const time = document.querySelector('#timer');
      this.selectedTime = time.value;
      if (this.selectedTime === '全部資料') {
        this.cacheDetals = this.details;
      } else {
        const timeStart = `${this.selectedTime.substring(0, 2)}00`;
        const timeEnd = `${this.selectedTime.substring(8, 10)}00`;
        this.cacheDetals = [];
        this.details.forEach((element) => {
          const enterTime =
            element.time.substring(0, 2) + element.time.substring(3, 5);
          if (enterTime > timeStart && enterTime < timeEnd) {
            this.cacheDetals.push(element);
          }
        });
      }
    },
    changeCard(item) {
      const customerTime =
        item.time.substring(0, 2) + item.time.substring(3, 5);
      if (customerTime < 1200) {
        this.time = `上午${item.time}`;
      } else {
        this.time = `下午${item.time}`;
      }
      this.gender = item.gender;
      this.age = item.age;
      this.style = item.style;
      this.recommandation = item.recommandation;
      this.imgUrl = item.imgUrl;
    },
  },

  computed: {
    totalUsers() {
      return this.cacheDetals.length;
    },
    totalPages() {
      return Math.ceil(this.totalUsers / this.users_per_page);
    },
    getUsersByPage() {
      // 計算起始index
      const startIndex = (this.selectedPage - 1) * this.users_per_page;
      return this.cacheDetals.slice(
        startIndex,
        startIndex + this.users_per_page,
      );
    },
  },
};
</script>

<style scoped lang="scss">
$main_color: #c180d3;

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
    display: flex;
    flex-direction: column;
    padding: 1rem;
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
          max-width: 230px;
          height: 230px;
          background-color: #eee;
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
    .boardTopic {
      padding-bottom: 1rem;
      font-size: 1.5rem;
      letter-spacing: 3px;
      text-align: center;
    }
    .boardFlow {
      height: 100%;
      margin-left: 1rem;
      padding: 1rem;
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
          .customarCard {
            position: relative;
            height: 80px;
            align-items: center;
            border-radius: 10px;
            background-color: #fefefe;
            box-shadow: 0 10px 10px -15px rgba(109, 94, 194, 0.4);
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

//navigation

.navigation {
  .page-link {
    color: $main_color;
  }
}

@media screen and (max-width: 768px) and (-webkit-min-device-pixel-ratio: 2) {
}
</style>
