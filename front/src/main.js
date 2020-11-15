import Vue from "vue";
import App from "./App.vue";
import VueTailwind from "vue-tailwind";
import store from "./store";
import router from "./router";
import Axios from "axios";

import _ from 'lodash';    
Object.defineProperty(Vue.prototype, '$_', { value: _ });

import './assets/css/tailwind.css'
import './assets/fonts/stylesheet.css'
import Unicon from 'vue-unicons'

import { uniSetting, uniPlusSquareMonochrome, uniBoxMonochrome, uniCube, uniChartMonochrome, uniTimes  } from 'vue-unicons/src/icons'
let iconsdefault = [uniSetting, uniPlusSquareMonochrome, uniBoxMonochrome, uniCube, uniChartMonochrome, uniTimes ]
import icons from './components/ui/icons'
let iconscon = icons.concat(iconsdefault)
console.log(iconscon)
Unicon.add(iconscon)

Vue.use(Unicon)

// Axios setup
Axios.interceptors.request.use(
  (config) => {
    let token = localStorage.getItem("user-token");
    if (token) {
      config.headers["Authorization"] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Store setup
router.beforeEach((to, from, next) => {
  if (!to.matched.some(record => record.meta.isPublic)) {
    if (!store.getters.isAuthenticated) {
      next({ name: 'Login' })
    } else {
      next()
    }
  } else {
    next() 
  }
})

const settings = {
  //...
};
Vue.use(VueTailwind, settings);

Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
  store,
  router
}).$mount("#app");
