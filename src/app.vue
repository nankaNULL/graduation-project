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
  font-size:12px;
}
ul,li{margin:0; padding:0}
li{list-style: none;}
#app {
  height: 100%;
}
.clearfix{
  overflow: hidden;
}
</style>
