import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // 存储token
    username: sessionStorage.getItem('username') ? sessionStorage.getItem('username') : ( localStorage.getItem('username') ? localStorage.getItem('username') : '' ),
    Authorization: sessionStorage.getItem('Authorization') ? sessionStorage.getItem('Authorization') : ( localStorage.getItem('Authorization') ? localStorage.getItem('Authorization') : '' )
  },
  mutations: {
    changeLogin (state, user) {
      state.Authorization = user.Authorization;
      sessionStorage.setItem('Authorization', user.Authorization);
      sessionStorage.setItem('username', user.username);
      if(user.remember){
        localStorage.setItem('Authorization', user.Authorization);
        localStorage.setItem('username', user.username);
      }
    }
  },
  actions: {
  },
  modules: {
  }
})
