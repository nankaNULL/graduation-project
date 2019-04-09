<template>
  <div class="page-home">
    <HomeSearch></HomeSearch>
    <div class="home-cell">
      <div v-for="(item, key) in cellData" :key="key" class="cell-item" @click="handleParamsChange(item.name)">
        <img :src="item.src" alt="emm" width="24" height="24" >
        <p>{{item.name}}</p>
      </div>
    </div>
    <HomeList v-bind:myType="type"></HomeList>
  </div>
</template>
<script>
import Vue from 'vue';
import HomeSearch from './components/homeSearch';
import HomeList from './components/homeList';

export default {
  name: "home",
  components:{
    HomeSearch,
    HomeList
  },
  data() {
    return {
      cellData: [
        { name: '简餐', src:'' },
        { name: '包子粥店', src:'' },
        { name: '川湘菜', src:'' },
        { name: '汉堡薯条', src:'' },
        { name: '盖浇饭', src:'' },
        { name: '甜品', src:'' },
        { name: '香锅砂锅', src:'' },
        { name: '饺子馄饨', src:'' },
        { name: '韩国炸鸡', src:'' },
        { name: '米粉面馆', src:'' }
      ],
      type: '简餐'
    };
  },
  methods: {
    handleParamsChange (type) {
      this.type = type;
    }
  }
};
</script>
<style lang="scss" scoped>
.page-home{
  .home-cell{
    display: flex;
    flex-wrap: wrap;
    .cell-item{
      width:20%;
    }
    .mint-cell-wrapper{
      flex-wrap: wrap;
    }
  }
}
</style>