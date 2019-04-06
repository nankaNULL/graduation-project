<template>
  <div class="home-list">
    <div class="list-select">
      <div class="title" @click="handleOptionShow">
        <span>{{optionList[params.optionId].name}}</span>
        <!-- <span>icon</span> -->
        <i class="mint-toast-icon mintui mintui-back icon-back"></i>
      </div>
      <ul class="option-list" v-show="optionShow">
        <li v-for="(item, key) in optionList" :key="key" @click="handleSelect(item.id)" 
          :style="params.optionId === item.id ? 'color: yellow' : null"> {{item.name}}</li>
      </ul>
    </div>
    <div
      v-infinite-scroll="loadMore"
      infinite-scroll-disabled="loading"
      infinite-scroll-distance="10">
      <div v-for="(item,key) in list" :key="key" class="cell-item" @click="handleTurnToPage(item)">
        <div class="cell-item-l">
          <img class="item-image" :src="item['image_path']" :alt="item.name">
        </div>
        <div class="cell-item-r">
          <h3>{{item.name}}</h3>
          <div class="clearfix">
            <p style="float:left">月售: <span>{{item[item.recommend+'_recent_order_num']}}</span></p>
            <p style="float:right;">
              <span>{{item[item.recommend+'_lead_time']}}</span>分钟 
              <span>{{1000 > item.distance ? item.distance + 'm' : (item.distance/1000).toFixed(2) + 'km'}}</span>
            </p> 
          </div>
          <p>起送 &yen; <span>{{item[item.recommend+'_order_amount']}}</span> 配送 &yen; <span>{{item[item.recommend+'_delivery_fee']}}</span> </p>
          <p>推荐渠道：<span>{{item.recommend === 'elm' ? '饿了么' : '美团'}}</span> </p>
        </div>
      </div>
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
import { API } from "@/api/index.js";
export default {
  name: "homeList",
  props: ['myType'],
  data() {
    return {
      list: [],
      loading: false,
      optionList: [{
          name:'距离最近',
          id:'0'
        },{
          name:'配送速度',
          id:'1'
        },{
          name:'评分',
          id:'2'
        },{
          name:'起送价最低',
          id:'3'
        },{
          name:'配送费最低',
          id:'4'
        },{
          name:'月售由高到低',
          id:'5'
        }],
      optionShow: false,
      
      params:{
        optionId: 0,
        type: this.myType,
      }
    };
  }, 
  watch:{
    myType:function(type){
      this.params.type = type;
      this.list = [];
      this.getShopList()
      this.loadMore();
    }
  },
  mounted: function() {
    this.getShopList(this.params.optionId);
  },
  methods: {
    // 获取列表
    getShopList (sortId) {
      API.getShopList({sortId}).then((result) => {
        result.forEach(item => {
          if (item['image_path'].slice(0,4) !== 'http' ){
            let imgType = item['image_path'].slice(-3) == 'png' ? 'png' : 'jpeg';
            item['image_path'] = 'https://fuss10.elemecdn.com/'+item['image_path'].slice(0,1)+'/'+item['image_path'].slice(1,3)+'/'+item['image_path'].slice(3)+'.'+imgType+'?imageMogr/format/webp/thumbnail/!130x130r/gravity/Center/crop/130x130/';
          }
        })
        this.list = result;
      })
    },
    // 选择框的弹出
    handleOptionShow () {
      this.optionShow = !this.optionShow;
    },
    // 选择框的选择
    handleSelect (optionId) {
      this.params.optionId = optionId;
      this.optionShow = false;
      this.list = [];
      this.getShopList(optionId)
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
    // 跳转到商品列表
    handleTurnToPage(shop) {
      const { elm_sid, mt_sid, recommend } = shop;
      this.$router.push({ path:'/shop', query:{ id: elm_sid || mt_sid, recommend: recommend }})
    }
  }
};
</script>
<style lang="scss">
  .home-list{
    border-top: 1px solid #e5e5e5;
    .list-select{
      .title, .option-list>li{
        padding: 15px 20px;
      }
      .title{
        font-size: 14px;
        .icon-back{
          display: inline-block;
          transform: rotate(-90deg);
        }
      }
      .option-list{
        &>li{
          border-bottom: 1px solid #e5e5e5;
          &:last-child{border:0}
        }
      }
    }
    
    .cell-item{
      padding: 10px;
      overflow: hidden;
      border-bottom : 1px solid #e5e5e5;
      .cell-item-l, .cell-item-r{ float: left;}
      .cell-item-l{
        padding: 10px 20px 0 0;
        .item-image{
          display: inline-block;
          height:130px;
          width:130px;
        }
      }
      .cell-item-r{
        width: calc(100% - (150px));
      }
    }
  }
</style>