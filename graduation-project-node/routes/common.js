var express = require("express");
var pool = require("../pool.js");
var util = require("./util.js");
var router = express.Router();

router.get('/searchShop', (req, res) => {
  var name = req.query.name;
  pool.query(`select * from final_shop where name like '%${name}%'`, (err, result) => {
    if ( err ) throw err;
    var response = {};
    if ( result.length > 0 ) {
      response.result = true;
      response.data = util.listSort(result, 0);
      response.message = '成功'
    } else {
      response.result = false;
      response.message = '不存在'
    }
    res.send(response)
  })
})

module.exports = router;