import Vue from "vue";

const userState = {
  userInfo: {},
};
const userMutations = {
  setUser(state, payload) {
    Vue.set(state.userInfo, 'userName', payload.userName);
    Vue.set(state.userInfo, 'cookie', payload.cookie);
    // state.userInfo.userName = userName;
  },
  clearUser(state) {
    state.userInfo = {};
  },
};
export default {
  namespaced: true,
  state: userState,
  mutations: userMutations,
};
