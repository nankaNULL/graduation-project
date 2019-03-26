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
        <img src="" alt="头像" class="img-avator">
      </div>
      <div class="shop-info">
        <h4>eemmm</h4>
        <!-- <p>评价<span>1</span> | 月售 <span>123</span>单 | 时间<span>29</span>分钟</p>
        <div>
          <span>满减</span>
          <span>29-16</span>
        </div> -->
      </div>
    </div>
    <div class="shop-content">
      <mt-navbar v-model="selected">
        <mt-tab-item id="1">商品列表</mt-tab-item>
        <mt-tab-item id="2">商家详情</mt-tab-item>
      </mt-navbar>
      <mt-tab-container v-model="selected">
        <mt-tab-container-item id="1">
          <ComponentList></ComponentList>
        </mt-tab-container-item>
        <mt-tab-container-item id="2">
          <StoreInfo></StoreInfo>
        </mt-tab-container-item>
      </mt-tab-container>
    </div>
  </div>
</template>
<script>
import { Navbar, TabItem } from 'mint-ui';
import ComponentList from './components/list.vue';
import StoreInfo from './components/storeInfo.vue';
export default {
  name: "shop",
  components:{
    ComponentList,
    StoreInfo
  },
  data() {
    return {
      loading: false,
      list: [],
      wrapperHeight: 0,
      selected: '1'
    };
  },
  methods: {
    loadMore() {
      this.loading = true;
      setTimeout(() => {
        let last = this.list[this.list.length - 1] || 0;
        for (let i = 1; i <= 10; i++) {
          this.list.push(last + i);
        }
        this.loading = false;
      }, 2000);
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
      border: 1px solid black;
      img{ 
        position:absolute;
        bottom:-30px;
        left: 50%;
        height:60px;
        width:60px;
        margin-left: -30px;
        border: 1px solid black; 
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