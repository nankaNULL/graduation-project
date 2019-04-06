export default {
  getHomeData:{
    method:'get',
    url:'/mock/success.json'
  },
  // 获取首页列表
  getShopList:{
    method:'get',
    url:'/api/shop/getShopList'
  },
  // 获取商品列表
  getFoodList:{
    method:'get',
    url:'/api/food/getFoodList'
  },
  // 获取商品详情
  getFoodInfo:{
    method:'get',
    url:'/api/food/getFoodInfo'
  }
}
