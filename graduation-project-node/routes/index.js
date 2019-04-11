var express = require("express");
var pool = require("../pool");
var util = require("./util");
var router = express.Router();

// 店铺列表数据获取
router.get("/getShopList", (req, res) => {
  var sortId = req.query.sortId || 0;
  pool.query("select * from final_shop", (err, result) => {
    if ( err ) throw err;
    if ( result.length > 0 ) {
      res.send(util.listSort(result, sortId))
    }
  })
});

// 店铺详情
router.get("/getShopInfo", (req, res) => {
  var sid = req.query.sid;
  var type = sid.slice(0,1) == 'E' ? 'elm_sid' : 'mt_sid'
  pool.query("select * from final_shop where " + type + "=?", sid, (err, result) => {
    if ( err ) throw err;
    if ( result.length > 0 ) {
      res.send(result)
    }
  })
});

// 店铺分类
router.get('/classify', (req, res) => {
  var type = req.query.type;
  var sortId = req.query.sortId || 0;
  pool.query("select * from final_shop where flavors = ?",type,(err, result) => {
    if (err) throw err;
    if ( result.length > 0 ) {
      res.send(util.listSort(result, sortId));
    } 
  })
})

module.exports = router;