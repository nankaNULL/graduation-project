var express = require("express");
var pool = require("../pool");
var util = require("./util");
var router = express.Router();

// 获取最大减免额度百分比
function getMaxSub (str, price) {
	let arr = str.replace(/[^0-9]+/g,",").split(",").slice(1);
	let min = 1000, mini = 1000;
	arr = arr.filter(function (s) {
    return s && s.trim(); // 注：IE9(不包含IE9)以下的版本没有trim()方法
	});
	// console.log(arr)
	arr.forEach((item, index) => {
		if ( index % 2 == 0 && item && index < arr.length - 1 && item >= price ){
			let point = (item - arr[index + 1]) / item;
			if ( min > point ) min = point;
		}
	})
	for(let i=0; i < arr.length; i++){
		if (i % 2 == 0 && arr[i] >= price) {
			mini = i;
			break;
		}
	}
	// console.log(price,min === 1000 ? null : (mini == 0 ? null : min),mini === 0 ? null : arr[mini+1])
	return {
		min: min === 1000 ? null : (mini == 0 ? null : min),
		maxCut: mini === 0 ? null : arr[mini-1]
	}
}

// 商品列表数据获取
function getFood (response, {type, shopId}) {
	return new Promise((resolve, reject) => {
		pool.query("select * from final_food where " + type + "=?", shopId, (err, result) => {
			if ( err ) throw err;
			if ( result.length > 0 ) {
				let newResult = [];
				let elm_str = response.shop['elm_sale_cut'];
				let mt_str = response.shop['mt_sale_cut'];
				
				result.forEach(item => {
					const channel = ['elm','mt'];
					// const channel = ['elm'];
					let maxSub = {};
					maxSub['elm_maxSub'] = elm_str && getMaxSub(elm_str, item['elm_price']);
					maxSub['mt_maxSub'] = mt_str && getMaxSub(mt_str, item['mt_price']);
					channel.forEach( channelItem => {
						if (item[channelItem + '_price']) {
							let maxCut = item[channelItem + '_price'] - (maxSub[channelItem+'_maxSub'].maxCut || 0);
							console.log(item[channelItem + '_price'],(maxSub[channelItem+'_maxSub'].maxCut || 0),maxCut)
							let compCut = maxSub[channelItem+'_maxSub'].min ? (maxSub[channelItem+'_maxSub'].min * item[channelItem + '_price']) : 100000;
							console.log(maxSub[channelItem+'_maxSub'].min,(maxSub[channelItem+'_maxSub'].min * item[channelItem + '_price']),compCut)
							item[channelItem + '_sub_price'] = maxCut < compCut ? maxCut : compCut;
							console.log(item[channelItem + '_sub_price'])
						}
					})
					if (item['elm_sub_price'] && item['mt_sub_price']) {
						if (item['elm_sub_price'] == item['mt_sub_price'] ) {
							item['elm_month_sales'] > item['mt_month_sales'] ? item.recommend = 'elm' : item.recommend = 'mt'
						} else {
							item['elm_sub_price'] < item['mt_sub_price'] ? item.recommend = 'elm' : item.recommend = 'mt'
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