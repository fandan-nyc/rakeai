// store/index.js
import Vue from "vue";
import Vuex from "vuex";
import userInfo from "./user";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    userInfo,
  },
});
