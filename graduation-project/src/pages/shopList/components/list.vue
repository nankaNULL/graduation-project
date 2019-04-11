<template>
  <div class="component-list">
    <div class="list-item" v-for="(item,key) in shopList" :key="key" @click="handleTurnToPage(item)">
      <div class="item-l">
        <img :src="item['image_path']" alt="">
      </div>
      <div class="item-r">
        <div>
          <h3>{{item.name}}</h3>
          <p class="text-ellipsis">{{item.description}}</p>
          <p style="color:red;font-size:16px">&yen;<span>{{item[item.recommend+'_sub_price']&&item[item.recommend+'_sub_price'].toFixed(2)}}</span></p>
          <p>推荐渠道：{{item.recommend === 'elm' ? '饿了么' : '美团' }}</p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "component-list",
  props: ['shopInfo','foodList','recommend'],
  data() {
    return {
      shopList: []
    };
  },
  watch:{
    foodList: function( info ){
      this.shopList = info;
    }, 
  },
  methods: {
    handleTurnToPage (food) {
      const { recommend } = food;
      this.$router.push({ path:'/goodInfo', query:{ id: food[recommend+'_fid'], recommend: recommend }})
    },
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
  .component-list{
    .list-item{
      display: flex;
      border-bottom: 1px solid #e5e5e5;
      padding: 20px;
      .item-l{
        img{
          display: inline-block;
          height:75px;
          width: 75px;
        }
      }
      .item-r{
        margin-left: 20px;
        h3{padding:0;margin:0}
      }
    }
  }
</style>