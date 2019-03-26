<template>
  <div>
    <mt-header title="商品详情">
      <mt-button
        slot="left"
        icon="more"
        @click.native="handleMore"
      ></mt-button>
    </mt-header>
    <div class="good-info">
      <img src="" alt="">
      <h3>{{goodName}}</h3>
      <div class="item">
        <h4>饿了么</h4>
        <p>月售：{{elm.monthSale}}</p>
        <p>赞：{{elm.zan}}</p>
        <p>价格：{{elm.price}}</p>
      </div>
      <div class="item">
        <h4>美团</h4>
        <p>月售：{{elm.monthSale}}</p>
        <p>赞：{{elm.zan}}</p>
        <p>价格：{{elm.price}}</p>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "homePage",
  data() {
    return {
      goodName:'11',
      elm:{
        monthSale:100,
        zan:1,
        price: 10.00
      }
    };
  },
  methods: {
    handleMore() {
      console.log("点击更多!");
    }
  }
};
</script>
<style lang="scss" scoped>
  .good-info{
    &>img{
      display: inline-block;
      height: 100px;
      width: 100%;
      border: 1px solid black;
    }
    &>h3, .item{ padding: 0 15px }
    .item{
      border-top: 1px solid #e5e5e5;
    }
  }
</style>