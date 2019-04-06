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
      <h3>{{foodInfo.name}}</h3>
      <div class="item" >
        <h3>饿了么</h3>
        <div v-if="JSON.stringify(foodInfo.elm)!='{}'">
          <p><span>月售：{{foodInfo.elm['month_sales']}}</span> <span class="ml-10">赞：{{foodInfo.elm['satisfy_rate']}}</span></p>
          <!-- <p></p> -->
          <p style="color:red">价格：&yen;{{foodInfo.elm.price}}</p>
        </div>
        <div v-else>
          <p>暂无数据</p>
        </div>
      </div>
      <div class="item">
        <h3>美团</h3>
        <div v-if="JSON.stringify(foodInfo.mt)!='{}'">
          <p>月售：{{foodInfo.mt['month_sales']}}</p>
          <p>赞：{{foodInfo.mt['satisfy_rate']}}</p>
          <p style="color:red">价格：&yen;{{foodInfo.mt.price}}</p>
        </div>
        <div v-else>
          <p>暂无数据</p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { API } from "@/api/index.js";
export default {
  name: "homePage",
  data() {
    return {
      foodId: this.$route.query.id,
      recommend: this.$route.query.recommend,
      foodInfo: {elm:{}, mt:{}},
    };
  },
  mounted: function() {
    this.getFoodInfo();
  },
  methods: {
    getFoodInfo () {
      API.getFoodInfo({
        fid: this.foodId, 
        recommend: this.recommend
      }).then((res) => {
        let result = res[0];
        let food = { 
          elm:{}, 
          mt:{},
          name:result.name,
          image_path: result['image_path'],
          description: result.description
        };
        const datas = ['month_sales', 'satisfy_rate', 'price'];
        const channels = ['elm', 'mt'];
        channels.forEach(channel => {
          datas.forEach(data => {
            if (result[channel + '_' + data] == 0 || result[channel + '_' + data]){
              food[channel][data] = result[channel + '_' + data];
              // console.log(result[channel + '_' + data])
            }
          })
        })
        this.foodInfo = food;
      })
    },
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
    &>h3, .item{ padding: 10px 20px }
    .item{
      border-top: 1px solid #e5e5e5;
    }
  }
</style>