//连接mysql数据库服务器
var mysql = require("mysql");
var pool = mysql.createPool({
	host:'127.0.0.1',
	port:3306,
	user:'root',
	password:'970429',
	database:'final',
	connectionLimit:10
});

module.exports = pool;