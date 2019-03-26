<template>
  <div class="home-list">
    <div class="list-select">
      <div class="title" @click="handleOptionShow">
        <span>{{params.optionId}}</span>
        <span>icon</span>
      </div>
      <ul class="option-list" v-show="optionShow">
        <li v-for="(item, key) in optionList" :key="key" @click="handleSelect(item)" 
          :style="params.optionId === item ? 'color: yellow' : null"> {{item}}</li>
      </ul>
    </div>
    <div
      v-infinite-scroll="loadMore"
      infinite-scroll-disabled="loading"
      infinite-scroll-distance="10">
      <mt-cell v-for="(item,key) in list" :key="key" class="cell-item">
        <div>
          <img src="" alt="">
        </div>
        <div>
          <h4>jeep </h4>
          <div class="clearfix">
            <p style="float:left">月售<span>1423</span></p>
            <p style="float:right"><span>30</span>分钟 <span>1.3</span>km</p> 
          </div>
          <p>起送 &yen; <span>1</span> 配送 &yen; <span>1</span> 人均 &yen; <span>11</span></p>
        </div>
      </mt-cell>
      <p
        v-show="loading"
        class="page-infinite-loading"
      >
        <mt-spinner type="fading-circle"></mt-spinner>
        加载中...
      </p>
    </div>
  </div>
</template>
<script>
import Vue from 'vue';
export default {
  name: "homeList",
  props: ['myType'],
  data() {
    return {
      list: [],
      loading: false,
      optionList: ['综合排序','配送速度','评分','起送价最低','配送费最低','人均由低到高'],
      optionShow: false,
      
      params:{
        optionId:'综合排序',
        type: this.myType,
      }
    };
  }, 
  watch:{
    myType:function(type){
      this.params.type = type;
      this.list = [];
      this.loadMore();
    }
  },
  methods: {
    // 选择框的弹出
    handleOptionShow () {
      this.optionShow = !this.optionShow;
    },
    // 选择框的选择
    handleSelect (option) {
      this.params.optionId = option;
      this.optionShow = false;
      this.list = [];
      this.loadMore();
    },
    // 列表加载
    loadMore() {
      this.loading = true;
      setTimeout(() => {
        let last = this.list[this.list.length - 1];
        for (let i = 1; i <= 10; i++) {
          this.list.push(last + i);
        }
        this.loading = false;
      }, 2500);
    },
  }
};
</script>
<style lang="scss" scoped>
  .home-list{
    border-top: 1px solid #e5e5e5;
    .list-select{
      .title, .option-list>li{
        padding: 15px 20px;
      }
      .option-list{
        &>li{
          border-bottom: 1px solid #e5e5e5;
          &:last-child{border:0}
        }
      }
    }
  }
</style>