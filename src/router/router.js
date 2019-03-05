import Vue from 'vue'
import Router from 'vue-router'
import MainLayout from '../layout/mainLayout';
import NotFoundComponent from '../pages/error/404';
import Login from '@/pages/login'
import ShoppingCart from '@/pages/shoppingCart'
import HomePage from '@/pages/homePage'
import ShopList from '@/pages/shopList'
Vue.use(Router)
export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: MainLayout,
      children: [{
        path: '/index',
        component: Login
      }, {
        path: '/cart',
        component: ShoppingCart
      }, {
        path: '/home',
        component: HomePage
      }, {
        path: '/shop',
        component: ShopList
      }]
    },
    {
      path: '*', component: NotFoundComponent
    }
  ]
})
