<template>
  <div class="store-info">
    <div class="info-item">
      <mt-cell class="title"
        title="商家信息"
      ></mt-cell>
      <mt-cell
        title="姓名"
        :value="userData.userName"
      ></mt-cell>
      <mt-cell
        title="地址"
        :value="userData.address"
      ></mt-cell>
      <mt-cell
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
      ></mt-cell>
    </div>
  </div>
</template>
<script>
export default {
  name: "store-info",
  data() {
    return {
      userData: {
        userName: "袋鼠云",
        address: "紫霞街",
        creator: "拖雷",
        englishName: "dtstack",
        yuanjing: "做国内领先的数据智能践行者",
        jiazhiguan: "客户第一、团队协作、专业、担当"
      }
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