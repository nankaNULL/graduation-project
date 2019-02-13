<template>
  <div>
    <mt-header title="商品">
      <mt-button
        slot="left"
        icon="more"
        @click.native="handleMore"
      ></mt-button>
    </mt-header>
    <div
      class="page-infinite-wrapper"
      ref="wrapper"
      :style="{ height: wrapperHeight + 'px' }"
    >
      <div
        class="page-infinite-list"
        v-infinite-scroll="loadMore"
        infinite-scroll-disabled="loading"
        infinite-scroll-distance="50"
      >
        <div
          v-for="(item,index) in list"
          :key="index"
          class="page-infinite-listitem"
        >
          <mt-cell
            :title="`第${item}名`"
            is-link
            value="小明"
          ></mt-cell>
        </div>
      </div>
      <p
        v-show="loading"
        class="page-infinite-loading"
      >
        <mt-spinner type="fading-circle"></mt-spinner>
        加载中...
      </p>
    </div>
  </div>
</template>
<script>
export default {
  name: "shop",
  data() {
    return {
      loading: false,
      list: [],
      wrapperHeight: 0
    };
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
.page-infinite-loading {
  text-align: center;
  height: 50px;
  line-height: 50px;
  div {
    display: inline-block;
    vertical-align: middle;
    margin-right: 5px;
  }
}
</style>