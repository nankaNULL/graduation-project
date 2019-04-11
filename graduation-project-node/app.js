var express = require("express");
var bodyParser = require("body-parser");
var session = require("express-session")

var app = express();
app.listen(3000, ()=>{
    console.log("服务已经启动")
});

app.use(bodyParser.urlencoded({
	extended:false
}));
app.use(session({
	secret: '128位随机字符串',
    resave: false,
    saveUninitialized: true,
}));

// //托管静态资源
// app.use(express.static("./public"));
app.use('/api/shop',require("./routes/index"));
app.use('/api/food',require("./routes/food"));
app.use('/api/common',require("./routes/common"));