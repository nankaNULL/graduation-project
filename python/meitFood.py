# coding=utf-8
import json
import re
from string import Template
from meitData import foodData 
import connectdb

# 店铺列表
def main():
  res = json.loads(foodData)
  if res.get("data"):
    categoryList = res.get("data").get('categoryList')
    get_connect(categoryList)

# 连接
def get_connect(categoryList):
  sid = '978227225210891'
  for item in categoryList:
    for food in item.get('spuList'):
      info = {}
      restaurant = food
      info['item_id'] = restaurant.get('spuId') #id
      info['name'] = restaurant.get('spuName') #名字
      info['description'] = restaurant.get('spuDesc') #描述
      info['image_path'] = restaurant.get('littleImageUrl') #图片路径
      info['month_sales'] = restaurant.get('saleVolume') #月售
      info['satisfy_rate'] = restaurant.get('praiseNum') #好评率
      info['price'] = restaurant.get('currentPrice') #价格

      # # sql操作
      if isExist(info['name']):
        sql = Template("update final_food set mt_fid=${mt_fid},mt_sid=${mt_sid},mt_month_sales=${mt_month_sales},mt_satisfy_rate=${mt_satisfy_rate},mt_price=${mt_price} where name='${name}'")
        sql = sql.substitute(mt_fid=info['item_id'],mt_sid=sid,mt_month_sales=info['month_sales'],mt_satisfy_rate=info['satisfy_rate'],mt_price=info['price'],name=info['name'])
        # print(sql)
        sta = connectdb.exe_update(cur,sql)
        if sta == 1:
          print('更新成功')
        else:
          print('更新失败')
      else:
        # print(info)
        sta = connectdb.exe_update(cur,"insert into final_food(mt_fid,mt_sid,name,description,image_path,mt_month_sales,mt_satisfy_rate,mt_price) values('%s','%s','%s','%s','%s','%f','%f','%f')" % (info['item_id'],sid,info['name'],info['description'],info['image_path'],info['month_sales'],info['satisfy_rate'],info['price']))
        if sta == 1:
          print('插入成功')
        else:
          print('插入失败')

# 是否已经存在该店铺
def isExist(name):
  sta = connectdb.exe_query(cur, "select * from final_food where name = '"+name+"'")
  if len(sta) > 0:
    return True
  return False

conn, cur = connectdb.conn_db()
main()
connectdb.exe_commit(cur)    # 注意！！ 一定要记得commit，否则操作成功了，但是并没有添加到数据库中
connectdb.conn_close(conn, cur)
