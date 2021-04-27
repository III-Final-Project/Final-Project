// Third-part
import Vuex from 'vuex';
import axios from 'axios';
import VueAxios from 'vue-axios';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
// Initial Vue
import Vue from 'vue';
import App from './App';
import router from './router/router';

// global implement
Vue.use(VueAxios, axios);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(Vuex);

// global middleware injection
Vue.prototype.$ajax = axios;
Vue.config.productionTip = false;
router.afterEach(() => {
  window.scrollTo(0, 0);
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: (h) => h(App),
}).$mount('#app');
