<template>
  <div class="component-list">
    <div class="list-item" v-for="(item,key) in shopList" :key="key">
      <div class="item-l">
        <img :src="item['image_path']" alt="">
      </div>
      <div class="item-r">
        <div>
          <h4>{{item.name}}</h4>
          <p>&yen;{{item.price}}</p>
          <!-- <p>推荐渠道：{{item.c}}</p> -->
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "component-list",
  props: ['shopInfo','foodList'],
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
      align-items: center;
      border-bottom: 1px solid #e5e5e5;
      &>div{padding: 20px}
      .item-l{
        img{
          display: inline-block;
          border:1px solid black;
          height:75px;
          width: 75px;
        }
      }
      .item-r{

      }
    }
  }
</style>