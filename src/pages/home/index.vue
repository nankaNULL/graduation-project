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
        { name: '美食', src:'' },
        { name: '超市便利', src:'' },
        { name: '蔬菜水果', src:'' },
        { name: '甜点饮品', src:'' },
        { name: '夜宵', src:'' },
        { name: '校园优选', src:'' },
        { name: '减免配送费', src:'' },
        { name: '龙虾烧烤', src:'' },
        { name: '浪漫鲜花', src:'' },
        { name: '甜蜜蛋糕', src:'' }
      ],
      type: '美食'
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