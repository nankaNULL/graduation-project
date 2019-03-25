<template>
  <div class="component-list">
    emmmm?????
  </div>
</template>
<script>
// import { Navbar, TabItem } from 'mint-ui';
export default {
  name: "component-list",
  data() {
    return {
      // loading: false,
      // list: [],
      // wrapperHeight: 0,
      // selected: '1'
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