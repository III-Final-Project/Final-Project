import Vue from 'vue';
import Router from 'vue-router';
// F0
import AIF000 from '@/pages/F0/AIF000';
import Signup from '@/components/F0/Signup';
import Login from '@/components/F0/Login';
import Reset from '@/components/F0/Reset';

// A0
import AIA000 from '@/pages/A0/AIA000';
import WebCam from '@/components/A0/WebCam';

import test from '@/components/A0/Charts/Analyze_by_color';

Vue.use(Router);

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '*',
      redirect: '/pages',
    },
    {
      path: '/pages',
      name: 'AIF000',
      component: AIF000,
    },
    {
      path: '/pages/signup',
      name: 'Signup',
      component: Signup,
    },
    {
      path: '/pages/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/Reset',
      name: 'Reset',
      component: Reset,
    },
    // 後台
    {
      path: '/admin',
      name: 'AIA000',
      component: AIA000,
    },
    {
      path: '/camera',
      name: 'camera',
      component: WebCam,
    },
    {
      path: '/test',
      name: 'Bar',
      component: test,
    },
  ],
});

export default router;
