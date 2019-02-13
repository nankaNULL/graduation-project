<template>
  <div>
    <mt-header title="我的">
      <mt-button
        slot="left"
        icon="more"
        @click.native="handleMore"
      ></mt-button>
    </mt-header>
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
</template>
<script>
export default {
  name: "homePage",
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
    handleMore() {
      console.log("点击更多!");
    }
  }
};
</script>
<style lang="scss" scoped>
</style>