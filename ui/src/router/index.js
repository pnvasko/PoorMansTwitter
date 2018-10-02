import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

import routes from './routes'

const Router = new VueRouter({
    mode: 'history',
    routes
})

export default Router
