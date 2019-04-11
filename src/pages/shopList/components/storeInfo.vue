<template>
  <div class="store-info">
    <div class="info-item">
      
      <mt-cell
        title="店铺名称"
        :value="shop.name"
      ></mt-cell>
      <mt-cell
        title="地址"
      ></mt-cell>
      <mt-cell style="text-align:right"
        :value="shop.address"
      ></mt-cell>
     <mt-cell
        title="电话"
        :value="shop.phone"
      ></mt-cell>
      <mt-cell
        title="营业时间"
        :value="shop['opening_hours']"
      ></mt-cell>
      <mt-cell
        title="商家信息"
      ></mt-cell>
      <mt-cell
        :value="shop.promotion_info"
      ></mt-cell>
    </div>
  </div>
</template>
<script>
export default {
  name: "store-info",
  props:['shop'],
  data() {
    return {
    };
  },
  methods: {
    
  }
};
</script>
<style lang="scss">
  .store-info{
    .info-item{
      .title{
        border: 0;
        .mint-cell-text{
          font-weight: bold;
        }
      }
    }
  }
</style>