<template>
  <div id="mainTpl">
    <router-view></router-view>
    <mt-tabbar
      v-model="selectedBar"
      fixed
      ref="mtTabbar"
    >
      <mt-tab-item
        id="首页"
        @click.native="routerPush"
      >
        <img
          slot="icon"
          src="https://zos.alipayobjects.com/rmsportal/sifuoDUQdAFKAVcFGROC.svg"
        >
        首页
      </mt-tab-item>
      <mt-tab-item
        id="商品"
        @click.native="routerPush"
      >
        <img
          slot="icon"
          src="https://gw.alipayobjects.com/zos/rmsportal/BTSsmHkPsQSPTktcXyTV.svg"
        >
        商品
      </mt-tab-item>
      <mt-tab-item
        id="购物车"
        @click.native="routerPush"
      >
        <img
          slot="icon"
          src="https://zos.alipayobjects.com/rmsportal/psUFoAMjkCcjqtUCNPxB.svg"
        >
        购物车
      </mt-tab-item>
      <mt-tab-item
        id="我的"
        @click.native="routerPush"
      >
        <img
          slot="icon"
          src="https://zos.alipayobjects.com/rmsportal/asJMfBrNqpMMlVpeInPQ.svg"
        >
        我的
      </mt-tab-item>
    </mt-tabbar>
  </div>
</template>
<script>
import { Tabbar, TabItem } from "mint-ui";
export default {
  components: {
    "mt-tabbar": Tabbar,
    "mt-tab-item": TabItem
  },
  data() {
    return {
      selectedBar: "首页",
      tab_ENUM: {
        首页: "index",
        商品: "shop",
        购物车: "cart",
        我的: "home"
      }
    };
  },
  mounted() {},
  methods: {
    routerPush() {
      const active = this.selectedBar;
      this.$router.push(this.tab_ENUM[active]);
    }
  }
};
</script>

<style lang="scss">
</style>
