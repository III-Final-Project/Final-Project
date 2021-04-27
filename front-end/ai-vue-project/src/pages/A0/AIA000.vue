<template>
  <div>
    <Header />
    <!-- Left-Side-Bar -->
    <div class="container">
      <button class="button-menu">Menu</button>
      <div class="main">
        <div class="sidebar">
          <ul>
            <li>
              <a href="#" @click.prevent="status = 'dashboard'"
                ><span>Dashboard</span></a
              >
            </li>
            <li>
              <a href="#" @click.prevent="status = 'datas'"
                ><span>Data Explore</span></a
              >
            </li>
            <li>
              <a href="#" @click.prevent="status = 'chart'"
                ><span>Charts</span></a
              >
            </li>
            <li>
              <a href="#"><span>Help & Support</span></a>
            </li>
          </ul>
        </div>
        <div class="right-content">
          <!-- dashboard -->
          <div class="page-content" v-if="status == 'dashboard'">
            <h1>Camera Wall</h1>
            <WebCam class="camera" />
            <AdminTable />
          </div>
          <!-- data -->
          <div class="page-content" v-if="status == 'datas'">
            <h1>Data Wall</h1>
            <AdminTable />
          </div>
          <!-- charts -->
          <div class="page-content" v-if="status == 'chart'">
            <h1>Charts</h1>
            <div class="search-box">
              <input type="search" placeholder="Search here..." />
              <button type="submit" class="search-btn">
                <img
                  :src="require('@/assets/icon/search_icon.png')"
                  alt="search-icon"
                />
              </button>
            </div>
            <div class="charts">
              <Pie />
              <Bar />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from '@/components/F0/Header';
import AdminTable from '@/components/A0/AdminTable';
import Pie from '@/components/A0/Charts/Pie';
import Bar from '@/components/A0/Charts/Bar';
import WebCam from '@/components/A0/WebCam';
import axios from 'vue-axios';

export default {
  name: 'AIA000',
  components: {
    AdminTable,
    Bar,
    Pie,
    Header,
    axios,
    WebCam,
  },
  data() {
    return {
      status: 'dashboard',
    };
  },
  mounted() {
    const menuButton = document.querySelector('.button-menu');
    const container = document.querySelector('.container');
    const pageContent = document.querySelector('.page-content');
    const responsiveBreakpoint = 991;

    if (window.innerWidth <= responsiveBreakpoint) {
      container.classList.add('nav-closed');
    }

    menuButton.addEventListener('click', () => {
      container.classList.toggle('nav-closed');
    });

    pageContent.addEventListener('click', () => {
      if (window.innerWidth <= responsiveBreakpoint) {
        container.classList.add('nav-closed');
      }
    });

    window.addEventListener('resize', () => {
      if (window.innerWidth > responsiveBreakpoint) {
        container.classList.remove('nav-closed');
      }
    });
  },
  methods: {},
};
</script>

<style scoped>
* {
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande',
    'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.right-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title {
  margin-top: 20vh;
  text-align: center;
}

.camera {
  background-color: white;
  width: 100%;
  height: 70vh;
  text-align: center;
}

.charts {
  overflow: hidden;
}

/* side bar */
.container {
  margin-top: 12vh;
  margin-left: 0;
  padding: 0;
  display: flex;
  height: 100vh;
  width: 100vw;
  flex-wrap: wrap;
  overflow: hidden;
}

.button-menu {
  background-color: #303f9e;
  color: #fff;
  border: #fff;
}

.main {
  height: calc(100% - 50px);
  display: flex;
  flex: 1;
}
.sidebar {
  height: 100vh;
  width: 250px;
  box-sizing: border-box;
  box-shadow: 0 0 2rem 0 rgb(0 0 0 / 5%);
  overflow: hidden;
  transition: width 0.5s ease;
}
.container.nav-closed .sidebar,
.container.nav-closed .header-logo {
  width: 0;
}
.sidebar ul {
  display: flex;
  flex-direction: column;
  padding: 5px;
}
.sidebar ul li {
  display: flex;
  align-items: center;
}
.sidebar ul li a {
  color: #000;
  display: flex;
  align-items: center;
  width: 100%;
  padding: 10px;
  white-space: nowrap;
}

.sidebar ul li a.active,
.sidebar ul li a:hover {
  background: #e8ecef;
}

.sidebar ul li span {
  margin-left: 10px;
  font-size: 16px;
  font-weight: 100;
}

.page-content {
  padding: 10px 20px;
  box-sizing: border-box;
  width: 100vh;
  flex: 1;
  text-align: center;
}

/* @media screen and (max-width: 991px) {
  .page-content {
    width: 100vw;
  }
}
@media screen and (max-width: 767px) {
  .header-logo {
    display: none;
  }
} */

.search-box {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 15vh;
}

input[type='search'] {
  box-shadow: 10px 10px 4px rgba(0, 0, 0, 0.4);
  background: #ffffff;
  border: 2px solid #e7693b;
  outline: none;
  width: 250px;
  height: 50px;
  border-radius: 15px 0 0 15px;
  font-size: 1.4em;
  font-weight: 300;
  padding: 0px 10px;
  font-family: 'Lato', sans-serif;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: #e7693b;
}

::placeholder {
  color: #81cce8;
  font-size: 0.8em;
}

.search-btn {
  box-shadow: 10px 10px 4px rgba(0, 0, 0, 0.4);
  height: 50px;
  width: 55px;
  outline: none;
  border-radius: 0 15px 15px 0;
  background: #e7693b;
  color: #ffffff;
  border: none;
  transition: all 0.3s ease;
}

.search-btn:hover {
  transition: all 0.3s ease;
}

.search-btn:hover img {
  font-size: 2.5em;
}

.search-btn img {
  font-size: 2.3em;
  width: 25px;
  height: 25px;
}
</style>
