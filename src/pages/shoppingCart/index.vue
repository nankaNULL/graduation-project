<template>
  <div class="shopppingCart">
    <mt-header title="购物车">
      <router-link
        to="/index"
        slot="left"
      >
        <mt-button icon="back">返回</mt-button>
      </router-link>
    </mt-header>
    <template v-for="(shop,index) in shops">
      <mt-cell
        :title="shop.name"
        :key="index"
      >
        <div icon="back">
          <span class="value">{{renderValue(shop.unitPrice,shop.number)}}¥</span>
          <span @click="diffValue(shop)">➖</span>
          <input
            class="shopNum"
            v-model="shop.number"
            disabled
          />
          <span @click="plusValue(shop)">➕</span>
        </div>
      </mt-cell>
    </template>
    <mt-cell
      title="总计"
      :label="totalCost"
    >
      <mt-button
        size="small"
        type="primary"
        @click.native="handleSubmit"
      >提交</mt-button>
    </mt-cell>
  </div>
</template>
<script>
import { Indicator, Toast } from "mint-ui";
import { API } from "@/api/index.js";
export default {
  name: "shoppingCart",
  data() {
    return {
      shopValue: 1,
      shops: [
        {
          name: "牛肉",
          unitPrice: 12,
          number: 1
        },
        {
          name: "羊肉",
          unitPrice: 22,
          number: 1
        },
        {
          name: "猪肉",
          unitPrice: 14,
          number: 1
        }
      ]
    };
  },
  computed: {
    totalCost() {
      let total = 0;
      this.shops.forEach(item => {
        total = total + item.unitPrice * item.number;
      });
      return total + "¥";
    }
  },
  methods: {
    diffValue(shop) {
      const value = shop.number - 1;
      if (value <= 0) {
        shop.number = 1;
      } else {
        shop.number = value;
      }
    },
    plusValue(shop) {
      shop.number += 1;
    },
    handleSubmit() {
      Indicator.open("提交中,请耐心等待...");
      setTimeout(() => {
        API.getHomeData().then(res => {
          Indicator.close();
          if (res.success) {
            Toast({
              message: "提交成功",
            });
          } else {
            Toast({
              message: "操作失败",
            });
          }
        });
      }, 1000);
    },
    renderValue(unitPrice, number) {
      return unitPrice * number;
    }
  }
};
</script>
<style lang="scss" scoped>
.shopppingCart {
  .value {
    margin-right: 1rem;
  }
  .shopNum {
    width: 50%;
    border: 1px solid #ddd;
    text-align: center;
  }
}
</style>