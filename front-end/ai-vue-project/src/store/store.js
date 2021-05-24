import Vue from 'vue';
import Vuex from 'vuex';
import User from '../service/user';

Vue.use(Vuex);
export default new Vuex.Store({
  state: {
    accessToken: null,
    user_name: null,
  },
  mutations: {
    updatedStorage(state, { access }) {
      state.accessToken = access;
    },
    updatedUsername(state, { userName }) {
      state.user_name = userName;
    },
  },
  actions: {
    userLogin(context, usercredentials) {
      return new Promise((resolve, reject) => {
        User.userLogin({
          user_name: usercredentials.user_name,
          user_password: usercredentials.user_password,
        })
          .then((response) => {
            context.commit('updatedStorage', {
              access: response.data.token,
            });
            context.commit('updatedUsername', {
              userName: usercredentials.user_name,
            });
            resolve();
          })
          .catch((err) => {
            reject(err);
          });
      });
    },
  },
});
