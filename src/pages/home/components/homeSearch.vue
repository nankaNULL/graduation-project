<template>
  <div class="home-search">
    <mt-search autofocus 
      v-model="storeSearch" 
      @keyup.enter.native="handleSearch()"
      >
      <ul class="search-list" >
        <li v-for="(item, key) in storeSearchList" :key="key" @click="handleToStore(item)">{{item}}</li>
      </ul>
    </mt-search>
  </div>
</template>
<script>
import Vue from 'vue';
import { Search } from 'mint-ui';
Vue.component(Search.name, Search);
export default {
  name: "homeSearch",
  data() {
    return {
      storeSearch:'',
      storeSearchList:['汉堡','芋说']
    };
  },
  methods: {
    // 顶部搜索店铺
    handleSearch () {
      console.log("emm",this.storeSearch)
    },
    // 搜索列表点击跳转
    handleToStore (storeName) {
      let path = this.$route.path;
      this.$router.push({  //核心语句
        path:'/select',   //跳转的路径
        query:{           //路由传参时push和query搭配使用 ，作用时传递参数
          id:storeName,  
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
      top:52px;
      left:0;
      bottom:0;
      right:0;
      &>li{
        padding:12px 20px;
        border-bottom:1px solid #e5e5e5;
      }
    }
  }
}
</style>