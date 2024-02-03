const userState = {
  userInfo: {},
};
const userMutations = {
  setUser(state, userName) {
    state.userInfo.userName = userName;
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
