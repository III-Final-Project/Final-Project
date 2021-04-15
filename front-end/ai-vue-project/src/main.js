import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
// import 'bootstrap/dist/css/bootstrap.css';
// import 'bootstrap-vue/dist/bootstrap-vue.css';
import Vue from 'vue';
import App from './App';
import router from './router/router';

Vue.config.productionTip = false;

router.afterEach(() => {
  window.scrollTo(0, 0);
});

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: (h) => h(App),
}).$mount('#app');
