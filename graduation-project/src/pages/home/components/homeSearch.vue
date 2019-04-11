<template>
  <div class="home-search">
    <mt-search autofocus 
      v-model="storeSearch" 
      @keyup.enter.native="handleSearch()"
      >
      <ul class="search-list" >
        <div class="list-empty" v-if="!storeSearchList.length">暂无结果</div>
        <li v-for="(item, key) in storeSearchList" :key="key" @click="handleToStore(item)">{{item.name}}</li>
      </ul>
    </mt-search>
  </div>
</template>
<script>
import Vue from 'vue';
import { API } from "@/api/index.js";
import { Search } from 'mint-ui';
Vue.component(Search.name, Search);
export default {
  name: "homeSearch",
  data() {
    return {
      storeSearch:'',
      storeSearchList:[]
    };
  },
  methods: {
    searchShop () {
      API.searchShop({name: this.storeSearch}).then((res) => {
        const { result, data, message } = res;
        if (result) {
          this.storeSearchList = data;
        } else {
          this.storeSearchList = []
        }
      })
    },
    // 顶部搜索店铺
    handleSearch () {
      this.storeSearchList = [];
      this.searchShop();
    },
    // 搜索列表点击跳转
    handleToStore (item) {
      this.$router.push({  //核心语句
        path:'/shop',   //跳转的路径
        query:{           //路由传参时push和query搭配使用 ，作用时传递参数
          id: item[item.recommend+'_sid'], 
          recommend: item.recommend
        }
      })
    }
  }
};
</script>
<style lang="scss" scoped>
.home-search{
  .mint-search{
    height:100%;
    .search-list{
      background:white;
      position: absolute;
      z-index: 99;
      top:52px;
      left:0;
      bottom:0;
      right:0;
      .list-empty{
        padding:20px;
        text-align: center;
        font-size: 16px;
      }
      &>li{
        padding:12px 20px;
        border-bottom:1px solid #e5e5e5;
      }
    }
  }
}
</style>