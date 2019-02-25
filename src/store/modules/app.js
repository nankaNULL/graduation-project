import { API } from "@/api/index.js";

const app = {
  state: {
    userData: []
  },
  mutations: {
    GET_USER_DATA: (state, userData) => {
      state.userData = userData
    }
  },
  actions: {
    getUserData({ commit }, params, cb) {
      API.getHomeData({}).then(ret => {
        console.log(ret);
        commit('GET_USER_DATA', ret.data || []);
      })
    }
  }
}

export default app
