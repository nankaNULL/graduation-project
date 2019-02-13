// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './app'
import router from './router/router'
import MintUI from 'mint-ui';
import 'mint-ui/lib/style.css';
import store from './store'

Vue.use(MintUI);
new Vue({
  el: '#root',
  router,
  store,
  components: {
    App
  },
  template: '<App/>'
})
