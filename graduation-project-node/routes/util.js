// 店铺列表排序
var listSort = (list, sortId) => { 
  let sortTypes = ['distance','lead_time','rating','order_amount','delivery_fee','recent_order_num'];
  let sortType = sortTypes[sortId];
  let newList = [];
  list.forEach(item => {
    const {elm_sid, mt_sid} = item;
    let choice = '';
    if (sortId == 0) {
      choice = elm_sid ? 'elm' : 'mt';
    }
    else {
      choice = elm_sid && mt_sid ? (item['elm_'+sortType] > item['mt_'+sortType] ? 'elm' : 'mt') : (elm_sid ? 'elm' : 'mt');
      item[sortType] = item[choice+'_'+sortType];
    }
    item.recommend = choice;
    newList.push(item)
  })
  newList.sort((a, b) => {
    return sortId == 5 ? b[sortType] - a[sortType] : a[sortType] - b[sortType]
  })
  return newList;
}

// 图片路径格式
var imgPathFormat = (theItem) => {
	let item = Object.assign({},theItem)
	if ( item['image_path'].slice(0,4) !== 'http' ){
		let imgType = item['image_path'].slice(-3) == 'png' ? 'png' : 'jpeg';
		item['image_path'] = 'https://fuss10.elemecdn.com/'+item['image_path'].slice(0,1)+'/'+item['image_path'].slice(1,3)+'/'+item['image_path'].slice(3)+'.'+imgType+'?imageMogr/format/webp/thumbnail/!130x130r/gravity/Center/crop/130x130/';
	}
	return item;
}

module.exports = {
  listSort,
  imgPathFormat
}