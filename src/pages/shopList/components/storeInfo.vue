<template>
  <div class="store-info">
    <div class="info-item">
      <mt-cell class="title"
        title="商家信息"
      ></mt-cell>
      <mt-cell
        title="店铺名称"
        :value="shop.name"
      ></mt-cell>
      <mt-cell
        title="地址"
        :value="shop.address"
      ></mt-cell>
      <!-- <mt-cell
        title="创始人"
        :value="userData.creator"
      ></mt-cell>
      <mt-cell
        title="公司英文简称"
        :value="userData.englishName"
      ></mt-cell>
      <mt-cell
        title="愿景"
        :value="userData.yuanjing"
      ></mt-cell>
      <mt-cell
        title="价值观"
        :value="userData.jiazhiguan"
      ></mt-cell> -->
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