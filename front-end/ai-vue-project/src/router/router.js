import Vue from 'vue';
import Router from 'vue-router';
// F0
import AIF000 from '@/pages/F0/AIF000';
import Signup from '@/components/F0/Signup';
import Login from '@/components/F0/Login';
import Reset from '@/components/F0/Reset';

Vue.use(Router);

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'AIF000',
      component: AIF000,
    },
    {
      path: '/Signup',
      name: 'Signup',
      component: Signup,
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/Reset',
      name: 'Reset',
      component: Reset,
    },
  ],
});

export default router;
