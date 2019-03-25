<template>
  <div class="page-home">
    <div class="home-cell">
      <div v-for="(item, key) in cellData" :key="key" class="cell-item">
        <img :src=item.src alt="emm" width="24" height="24">
        <p>{{item.name}}</p>
      </div>
    </div>
    <div className="home-list">
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
  </div>
</template>
<script>
export default {
  name: "home",
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
      list: [],
      loading: false
    };
  },
  methods: {
    handleMore() {
      console.log("点击更多!");
    },
    loadMore() {
      this.loading = true;
      setTimeout(() => {
        let last = this.list[this.list.length - 1];
        for (let i = 1; i <= 10; i++) {
          this.list.push(last + i);
        }
        this.loading = false;
      }, 2500);
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
.clearfix{
  overflow: hidden;
}
</style>