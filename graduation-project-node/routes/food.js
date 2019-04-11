var express = require("express");
var pool = require("../pool");
var util = require("./util");
var router = express.Router();

// 获取最大减免额度百分比
function getMaxSub (str) {
	let arr = str.replace(/[^0-9]+/g,",").split(",").slice(1);
	let pointLists = [];
	arr.forEach((item, index) => {
		if (index % 2 == 0)
			pointLists.push( (item - arr[index + 1]) / item );
	})
	return Math.min.apply(null,pointLists)
}

// 商品列表数据获取
function getFood (response, {type, shopId}) {
	return new Promise((resolve, reject) => {
		pool.query("select * from final_food where " + type + "=?", shopId, (err, result) => {
			if ( err ) throw err;
			if ( result.length > 0 ) {
				let newResult = [];
				let elm_str = '满22减13;满30减23;满45减26;满60减35';
				let mt_str = '满22减13;满30减23;满45减25;满60减35';
				let maxSub = {};
				maxSub['elm_maxSub'] = getMaxSub(elm_str);
				maxSub['mt_maxSub'] = getMaxSub(mt_str);
				result.forEach(item => {
					const channel = ['elm','mt'];
					channel.forEach( channelItem => {
						item[channelItem + '_price'] ? item[channelItem + '_sub_price'] = maxSub[channelItem+'_maxSub'] * item[channelItem + '_price'] : null;
					})
					if (item['elm_sub_price'] && item['mt_sub_price']) {
						if (item['elm_sub_price'] == item['mt_sub_price'] ) {
							item['elm_month_sales'] > item['mt_month_sales'] ? item.recommend = 'elm' : item.recommend = 'mt'
						} else {
							item['elm_sub_price'] > item['mt_sub_price'] ? item.recommend = 'elm' : item.recommend = 'mt'
						}
					} else {
						item['elm_sub_price'] ? item.recommend = 'elm' : item.recommend = 'mt';
					}
					newResult.push(util.imgPathFormat(item));
				})
				response.food = newResult;
				response.result = 'sucess';
				resolve(response)
			}
			else{
				reject(JSON.stringify({code:'404',result:'fail',message:'food not exist'}))
			}
		})
	})
}
function getShop (response, {type, shopId}) {
	return new Promise((resolve, reject) => {
		pool.query("select * from final_shop where " + type + "=?", shopId, (err, result) => {
			if ( err ) throw err;
			if ( result.length > 0 ) {
				response.shop = util.imgPathFormat(result[0]);
				resolve(response)
			}
			else{
				reject(JSON.stringify({code:'401',result:'fail',message:'shop not exist'}))
			}
		})
	})
}

router.get("/getFoodList", (req, res) => { 
	var shopId = req.query.shopId;
	var params = {
		shopId,
		type: shopId.slice(0,1) == 'E' ? 'elm_sid' : 'mt_sid'
	};
	var response = {};
	
	getShop(response, params)
		.then(() => getFood(response, params))
		.then((result) => res.send(result))
		.catch((error) => res.send(error))
});

// 商品详情信息获取
router.get("/getFoodInfo", (req, res) => {
	var fid = req.query.fid;
	var recommend = req.query.recommend;
	pool.query("select * from final_food where " + recommend + "_fid=?", fid, (err, result) => {
		if (err) throw err;
		if (result.length > 0 ){
			result.map(item => item['image_path'] = util.imgPathFormat(item)['image_path'])
			res.send(result);
		}else{
			res.send({code:'401',result:'fail',message:'food not exist'})
		}
		
	})
})

module.exports = router;