import Vue from 'vue'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-vue/dist/bootstrap-vue.css"

import App from './App.vue'

Vue.config.productionTip = false
Vue.use(BootstrapVue)

new Vue({
    el: '#app',
    router,
    render: h => h(App)
})

