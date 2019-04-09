<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "app"
};
</script>

<style lang="less">
body,
html {
  background-color: #fbf9fe;
  height: 100%;
  margin: 0;
  font-size:14px;
}
ul, li{margin:0; padding:0}
li{list-style: none;}
h3, p{margin:10px 0; padding:0;}
#app {
  height: 100%;
}
.clearfix{
  overflow: hidden;
}
.ml-10{
  margin-left: 10px;
}
.mr-10{
  margin-right: 10px;
}
.text-ellipsis{
  text-overflow: -o-ellipsis-lastline;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
}
</style>
