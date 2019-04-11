<template>
  <div class="mt-login">
    <mt-header
      title="basic"
    >
      <mt-button
        slot="left"
        icon="more"
        @click.native="handleMore"
      ></mt-button>
    </mt-header>
    <div>
      <mt-field
        label="用户名"
        placeholder="请输入用户名"
        v-model.trim="username"
      ></mt-field>
      <mt-field
        label="密码"
        placeholder="请输入密码"
        type="password"
        v-model.trim="password"
      ></mt-field>
    </div>
  </div>
</template>
<script>
import { Field, Header } from "mint-ui";
export default {
  name: "login",
  components: {
    "mt-field": Field,
    "mt-header": Header
  },
  data() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    handleMore() {
      console.log("点击了更多");
    }
  }
};
</script>
<style lang="scss" scoped>
</style>