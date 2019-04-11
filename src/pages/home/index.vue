<template>
  <div class="page-home">
    <HomeSearch></HomeSearch>
    <div class="home-cell">
      <div v-for="(item, key) in cellData" :key="key" class="cell-item" @click="handleParamsChange(item.name)">
        <img :src="item.src" alt="emm" width="50" height="50" >
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
        { name: '简餐', src:'https://fuss10.elemecdn.com/7/d8/a867c870b22bc74c87c348b75528djpeg.jpeg?imageMogr/format/webp/thumbnail/!90x90r/gravity/Center/crop/90x90/' },
        { name: '包子粥店', src:'https://fuss10.elemecdn.com/5/1a/dc885d2ce022d2ee60495acafb795jpeg.jpeg?imageMogr/format/webp/thumbnail/!90x90r/gravity/Center/crop/90x90/' },
        { name: '川湘菜', src:'https://fuss10.elemecdn.com/a/8a/ec21096d528b7cfd23cdd894f01c6jpeg.jpeg?imageMogr/format/webp/thumbnail/!90x90r/gravity/Center/crop/90x90/' },
        { name: '汉堡薯条', src:'https://fuss10.elemecdn.com/b/7f/432619fb21a40b05cd25d11eca02djpeg.jpeg?imageMogr/format/webp/thumbnail/!90x90r/gravity/Center/crop/90x90/' },
        { name: '盖浇饭', src:'https://fuss10.elemecdn.com/a/7b/b02bd836411c016935d258b300cfejpeg.jpeg?imageMogr/format/webp/thumbnail/!90x90r/gravity/Center/crop/90x90/' },
        { name: '甜品', src:'https://fuss10.elemecdn.com/7/d6/6f2631288a44ec177204e05cbcb93jpeg.jpeg?imageMogr/format/webp/thumbnail/!90x90r/gravity/Center/crop/90x90/' },
        { name: '香锅砂锅', src:'https://fuss10.elemecdn.com/e/c7/b7ba9547aa700bd20d0420e1794a8jpeg.jpeg?imageMogr/format/webp/thumbnail/!90x90r/gravity/Center/crop/90x90/' },
        { name: '饺子馄饨', src:'https://fuss10.elemecdn.com/0/1a/314b6da88ab6c7ae9828f91652d40jpeg.jpeg?imageMogr/format/webp/thumbnail/!90x90r/gravity/Center/crop/90x90/' },
        { name: '韩国炸鸡', src:'https://fuss10.elemecdn.com/a/78/0fb469b2da210827ec16896e00420jpeg.jpeg?imageMogr/format/webp/thumbnail/!90x90r/gravity/Center/crop/90x90/' },
        { name: '米粉面馆', src:'https://fuss10.elemecdn.com/e/89/185f7259ebda19e16123884a60ef2jpeg.jpeg?imageMogr/format/webp/thumbnail/!90x90r/gravity/Center/crop/90x90/' }
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
    background: white;
    .cell-item{
      width:20%;
      text-align: center;
    }
    .mint-cell-wrapper{
      flex-wrap: wrap;
    }
  }
}
</style>