import Vue from 'vue'
import Router from 'vue-router'
import MainLayout from '../layout/mainLayout';
import NotFoundComponent from '../pages/error/404';
import Login from '@/pages/login'
import ShoppingCart from '@/pages/shoppingCart'
import GoodInfo from '@/pages/goodInfo'
import ShopList from '@/pages/shopList'
import Home from '@/pages/home'
Vue.use(Router)
export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect:'/index',
      component: MainLayout,
      children: [{
        path: '/index',
        component: Home
      }, {
        path: '/cart',
        component: ShoppingCart
      }, {
        path: '/home',
        component: GoodInfo
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
