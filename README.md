# graduation-project

#### 项目说明
```
美食数据智能分析平台是通过对不同渠道的店铺以及店铺内商品信息进行分析，推荐最佳选购渠道的智能分析平台。
他具有根据距离远近、配送速度，评分等性能指标，对店铺信息进行智能排序的功能，
对店铺进行模糊搜素的功能，以及通过店铺分类进行智能筛选的功能。
所有信息（包括店铺以及商品信息）均通过一系列的分析后，将最优结果返回并展示。
graduation-project 是前端 vue + mint-ui + webpack
graduation-project-node 是后端 nodejs + express + mysql
python 是抓取到的数据 requests
```

#### 使用技术
```text
  vue, mint-ui, ko-script, nodejs, mysql, python...
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


