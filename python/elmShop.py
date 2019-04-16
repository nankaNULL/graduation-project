import requests
import json
from string import Template
import csv
import connectdb

def crawler_ele(page=0):
	
   def get_page(page):
      url = 'https://h5.ele.me/restapi/shopping/v3/restaurants?latitude=30.292853&longitude=120.016261&offset={page}&limit=8&terminal=h5'.format(page=page*8)
      headers = {
	  	   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
	   	'cookie': '_utrace=2f5126a3b54d1a0fc0ccf5c17e46804b_2019-03-25; cna=lT2iFLwXLXoCAXPp3iS9hbBo; ubt_ssid=nm1jl6v4wltmher7o7qt8l3fa9y0czwp_2019-03-25; UTUSER=256283994; eleme__ele_me=b803d7f10376b0440712b65fae06752d%3Acd995430132bb3138f806ffb05bb7f93d4018382; track_id=1553495931|b3f908ed22d66e975720bf1c552ff863627f65c893e0e17428|1af94e40b10ec8372159b82850324a65; USERID=256283994; SID=LgqgMpn9RHJhlJcfHoEAduAvZngFG8FI4dWA; isg=BJ2dqeidnaNB2XmIuEoQBf-ErHlXEm4JSHLl219izfQjFrxIJwj13K1HQUq1nenE; pizza73686f7070696e67=CPuz42fVoxnRVcVQ1x33fa7Yi_bsXs-3QA-gKZCLbXhJE9DcoZX1IkH-jckHAmtY'
		}
      re = json.loads(requests.get(url,headers=headers).text)
      return re

   re = get_page(page)
   
   if re.get('items'):
      items = re.get('items')
      get_connect(items)

   # print(re.get('has_next') == True)
   
   if re.get('has_next') == True and page < 8:
      print(page)
      crawler_ele(page+1)

def get_connect(items):
   for item in items:
      info = {}
      restaurant = item.get('restaurant')
      info['sid'] = restaurant.get('id') #id
      info['image_path'] = restaurant.get('image_path') #图片路径
      info['address'] = restaurant.get('address') #地址
      info['float_delivery_fee'] = restaurant.get('float_delivery_fee') #配送费
      info['name'] = restaurant.get('name') #名称
      info['order_lead_time'] = restaurant.get('order_lead_time') #配送时长
      info['distance'] = restaurant.get('distance') #距离
      info['float_minimum_order_amount'] = restaurant.get('float_minimum_order_amount') #起送价
      info['rating'] = restaurant.get('rating') #评分
      info['recent_order_num'] = restaurant.get('recent_order_num') #月销售量
      info['rating_count'] = restaurant.get('rating_count') #评分 统计
      info['flavors'] = restaurant.get('flavors')[0].get('name') #风味
      #满减
      businessInfo = json.loads(restaurant.get('business_info'))
      saleCuts = []
      for tag in businessInfo.get('lemon_support_tags'):
         text = tag.get('text')
         if text.find('减') != -1 and text.find('首单') == -1:
            saleCuts.append('满'+text)
      info['sale_cut'] = ';'.join(saleCuts)
      info['phone'] = restaurant.get('phone') #电话
      info['opening_hours'] = restaurant.get('opening_hours')[0] #营业时间
      info['promotion_info'] = restaurant.get('promotion_info') #描述
      if isExist(info['sid']):
         sql = Template("update final_shop set elm_rating=${elm_rating},elm_recent_order_num=${elm_recent_order_num},elm_rating_count=${elm_rating_count},sale_cut='${sale_cut}',phone='${phone}',opening_hours='${opening_hours}',promotion_info='${promotion_info}' where elm_sid='${elm_sid}'")
         sql = sql.substitute(elm_rating=info['rating'],elm_recent_order_num=info['recent_order_num'],elm_rating_count=info['rating_count'],sale_cut=info['sale_cut'],phone=info['phone'],opening_hours=info['opening_hours'],promotion_info=info['promotion_info'],elm_sid=info['sid'])
         # print(sql)
         sta = connectdb.exe_update(cur,sql)
         if sta == 1:
            print('更新成功')
         else:
            print('更新失败')
      else:
         sta = connectdb.exe_update(cur,"insert into final_shop(elm_sid, name, image_path, address, elm_delivery_fee, elm_lead_time, distance, elm_order_amount, elm_rating, elm_recent_order_num, elm_rating_count, flavors, elm_sale_cut, phone, opening_hours, promotion_info) values('%s','%s','%s','%s','%f','%f','%f','%f','%f','%f','%f','%s','%s','%s','%s','%s')" % (info['sid'], info['name'], info['image_path'], info['address'], info['float_delivery_fee'], info['order_lead_time'], info['distance'], info['float_minimum_order_amount'], info['rating'], info['recent_order_num'], info['rating_count'], info['flavors'],info['sale_cut'],info['phone'],info['opening_hours'],info['promotion_info']))
         if sta == 1:
            print('插入成功')
         else:
            print('插入失败')
   
def isExist(sid):
   sta = connectdb.exe_query(cur, "select * from final_shop where elm_sid = '" + sid + "'" )
   return len(sta)

conn, cur = connectdb.conn_db()
crawler_ele(0)
connectdb.exe_commit(cur)    # 注意！！ 一定要记得commit，否则操作成功了，但是并没有添加到数据库中
connectdb.conn_close(conn, cur)