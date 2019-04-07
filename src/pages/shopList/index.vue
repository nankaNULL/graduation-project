<template>
  <div class="page-shop-list">
    <mt-header title="商品">
      <mt-button
        slot="left"
        icon="more"
        @click.native="handleMore"
      ></mt-button>
    </mt-header>
    <div class="shop-top">
      <div class="top-img">
        <img :src="shopInfo['image_path']" class="img-background"/>
        <img :src="shopInfo['image_path']" alt="头像" class="img-avator" />
      </div>
      <div class="shop-info">
        <h2>{{shopInfo.name}}</h2>
        <p>推荐渠道：<span>美团</span> | 月售：<span>{{shopInfo[recommend+'_recent_order_num']}}</span>单 | 时间：<span>{{shopInfo[recommend+'_lead_time']}}</span>分钟</p>
        <div>
          <span>满减</span>
          <span>29-16</span>
        </div>
      </div>
    </div>
    <div class="shop-content">
      <mt-navbar v-model="selected">
        <mt-tab-item id="1">商品列表</mt-tab-item>
        <mt-tab-item id="2">商家详情</mt-tab-item>
      </mt-navbar>
      <mt-tab-container v-model="selected">
        <mt-tab-container-item id="1">
          <ComponentList v-bind:shopInfo="shopInfo" v-bind:foodList="list"></ComponentList>
        </mt-tab-container-item>
        <mt-tab-container-item id="2">
          <StoreInfo v-bind:shop="shopInfo"></StoreInfo>
        </mt-tab-container-item>
      </mt-tab-container>
    </div>
  </div>
</template>
<script>
import { Navbar, TabItem } from 'mint-ui';
import ComponentList from './components/list.vue';
import StoreInfo from './components/storeInfo.vue';
import { API } from "@/api/index.js";
export default {
  name: "shop",
  components:{
    ComponentList,
    StoreInfo
  },
  data() {
    return {
      loading: false,
      list: [], // 商品列表
      selected: '1',
      shopId: this.$route.query.id,
      recommend: this.$route.query.recommend,
      shopInfo: {}, // 店铺详情
      backgroundImageStyle:""
    };
  },
  mounted: function(){
    const shopId = this.$route.query.id;
    this.getFoodList(shopId)
  },
  watch: {
    backgroundImageStyle: function(){
      return "background-image:"+ this.shopInfo['image_path'] + "no-repeat"
    },
  },
  methods: {
    getFoodList (shopId) {
      API.getFoodList({ shopId }).then((res) => {
        const { result, message, shop, food} = res;
        if (result) {
          this.list = food;
          this.shopInfo = shop;
        } else {
          // 弹框
          console.log(message)
        }
      })
    }
  }
};
</script>
<style lang="scss">
.page-shop-list{
  .shop-top{
    .top-img{
      position: relative;
      height:75px;
      border: 1px solid #e5e5e5;
      .img-background{
        position: absolute;
        width: 100%;
        bottom:0;
        opacity: 0.95;
      }
      .img-avator{ 
        position:absolute;
        bottom:-18px;
        left: 50%;
        height:60px;
        width:60px;
        margin-left: -30px;
        border: 1px solid #e5e5e5;
      }
    }
  }
  .shop-info{
    text-align: center;
    padding: 20px;
  }
  .shop-content{
    margin-bottom: 55px;
  }
}
</style>