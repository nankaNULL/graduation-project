# graduation-project
毕设
#### 使用技术
```text
  vue, mint-ui, ko-script, nodejs, mysql, python...
```
#### 客户端渲染
```
本项目是客户端渲染版本
对于 HTTP/1.1 客户端，由 webpack 打包你的应用程序会尤其强大，因为在浏览器发起一个新请求时，
它能够减少应用程序必须等待的时间。对于 HTTP/2，你还可以使用代码拆分(Code Splitting)以及通过 
webpack 打包来实现最佳优化。
```

==========================

#### 安装教程

1、 安装依赖包。
```
npm install 或者cnpm install 或者yarn(推荐)

```

2、运行脚手架。
 ```
 yarn start

 ```

3、将会开启8080端口.
```
http://127.0.0.1:8080

```

===========================================

#### 项目结构

```text

├── public // 静态资源
├── src //项目的主要目录
│     │     ├── api //api接口
│     │     ├── pages //页面
│     │     ├── layout //布局
│     │     ├── constants //全局常量
│     │     ├── store //全局数据
│     │     ├── utils //提供一些小工具
│     │     ├── router //路由
│     │     ├── app.vue //主页面
│     │     └── main.js //应用的入口
├── ko.config //ko-script打包配置文件
└── package.json //node相关环境的配置文件

```

===========================================

#### 服务端结构

```text

├── routes // 路由表
├── app.js //入口
├── pool.js //数据库连接
└── package.json //相关环境的配置文件

```

**本项目wepack4，测试通过，快来体验吧！**

