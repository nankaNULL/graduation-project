# coding=utf-8
import json
import re
from string import Template
from meitData import shopData 
import connectdb

# 店铺列表
def main():
  res = json.loads(shopData)

  if res.get("data"):
    shopList = res.get("data").get('shopList')
    get_connect(shopList)

# 连接
def get_connect(shopList):
  for shop in shopList:
    info = {}
    restaurant = shop
    info['sid'] = restaurant.get('mtWmPoiId') #id
    info['name'] = restaurant.get('shopName') #名字
    info['image_path'] = restaurant.get('picUrl') #图片路径
    info['address'] = restaurant.get('address') #地址
    info['float_delivery_fee'] = float(re.findall(r"\d+\.?\d*",restaurant.get('shippingFeeTip'))[0]) #配送费
    info['order_lead_time'] = int(re.sub("\D", "", restaurant.get('deliveryTimeTip'))) #配送时长
    # 距离
    distance = float(re.findall(r"\d+\.?\d*",restaurant.get('distance'))[0])
    isKm = restaurant.get('distance').find('km')
    if isKm == -1:
      info['distance'] = distance
    else:
      info['distance'] = distance * 1000
    info['float_minimum_order_amount'] = int(re.sub("\D", "", restaurant.get('shippingFeeTip'))) #起送价
    info['rating'] = restaurant.get('wmPoiScore') / 10 #评分
    info['recent_order_num'] = int(re.sub("\D", "", restaurant.get('monthSalesTip'))) #月销售量
    
    # sql操作
    if isExist(info['name']):
      sql = Template("update final_shop set mt_delivery_fee=${mt_delivery_fee},mt_lead_time=${mt_lead_time},mt_order_amount=${mt_order_amount},mt_rating=${mt_rating},mt_recent_order_num=${mt_recent_order_num} where name='${name}'")
      sql = sql.substitute(mt_delivery_fee=info['float_delivery_fee'],mt_lead_time=info['order_lead_time'],mt_order_amount=info['float_minimum_order_amount'],mt_rating=info['rating'],mt_recent_order_num=info['recent_order_num'],name=info['name'])
      sta = connectdb.exe_update(cur,sql)
      if sta == 1:
        print('更新成功')
      else:
        print('更新失败')
    else:
      sta = connectdb.exe_update(cur,"insert into final_shop(mt_sid, name, image_path, address, mt_delivery_fee, mt_lead_time, distance, mt_order_amount, mt_rating, mt_recent_order_num) values('%s','%s','%s','%s','%f','%f','%f','%f','%f','%f')" % (info['sid'], info['name'], info['image_path'], info['address'], info['float_delivery_fee'], info['order_lead_time'], info['distance'], info['float_minimum_order_amount'], info['rating'], info['recent_order_num']))
      if sta == 1:
        print('插入成功')
      else:
        print('插入失败')

# 是否已经存在该店铺
def isExist(name):
  sta = connectdb.exe_query(cur, "select sid from final_shop where name = '"+name+"'")
  if len(sta) > 0:
    return True
  return False

conn, cur = connectdb.conn_db()
main()
connectdb.exe_commit(cur)    # 注意！！ 一定要记得commit，否则操作成功了，但是并没有添加到数据库中
connectdb.conn_close(conn, cur)



