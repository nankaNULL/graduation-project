<template>
  <div class="page-shop-list">
    <mt-header title="商品">
      <mt-button
        slot="left"
        icon="more"
        @click.native="handleMore"
      ></mt-button>
    </mt-header>
    <div class="shop-top">
      <div class="top-img">
        <img src="" alt="头像" class="img-avator">
      </div>
      <div class="shop-info">
        <h4>eemmm</h4>
        <p>评价<span>1</span> | 月售 <span>123</span>单 | 时间<span>29</span>分钟</p>
        <div>
          <span>满减</span>
          <span>29-16</span>
        </div>
      </div>
    </div>
    <div class="shop-content">
      <div class="tab">
        <div></div>
      </div>
      <mt-navbar v-model="selected">
        <mt-tab-item id="1">option A</mt-tab-item>
        <mt-tab-item id="2">option B</mt-tab-item>
        <mt-tab-item id="3">option C</mt-tab-item>
      </mt-navbar>

      <mt-tab-container v-model="selected">
        <mt-tab-container-item id="1">
          <ComponentList></ComponentList>
        </mt-tab-container-item>
        <mt-tab-container-item id="2">
          <div>emm2</div>
        </mt-tab-container-item>
        <mt-tab-container-item id="3">
          <div>emm3</div>
        </mt-tab-container-item>
      </mt-tab-container>
    </div>
    
    <!-- <div
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
    </div> -->
  </div>
</template>
<script>
import { Navbar, TabItem } from 'mint-ui';
import ComponentList from './components/list.vue';
export default {
  name: "shop",
  components:{
    ComponentList
  },
  data() {
    return {
      loading: false,
      list: [],
      wrapperHeight: 0,
      selected: '1'
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