import requests
import json
import connectdb

# 主函数
def crawler_ele(page=0):
	
   # 爬数据
   def get_page(shop_id):
      url = 'https://h5.ele.me/pizza/shopping/restaurants/'+shop_id+'/batch_shop?terminal=h5&latitude=30.29016&longitude=120.00914'
      headers = {
	  	   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
	   	'cookie': '_utrace=2f5126a3b54d1a0fc0ccf5c17e46804b_2019-03-25; cna=lT2iFLwXLXoCAXPp3iS9hbBo; ubt_ssid=nm1jl6v4wltmher7o7qt8l3fa9y0czwp_2019-03-25; UTUSER=256283994; eleme__ele_me=b803d7f10376b0440712b65fae06752d%3Acd995430132bb3138f806ffb05bb7f93d4018382; track_id=1553495931|b3f908ed22d66e975720bf1c552ff863627f65c893e0e17428|1af94e40b10ec8372159b82850324a65; USERID=256283994; SID=LgqgMpn9RHJhlJcfHoEAduAvZngFG8FI4dWA; isg=BJ2dqeidnaNB2XmIuEoQBf-ErHlXEm4JSHLl219izfQjFrxIJwj13K1HQUq1nenE; pizza73686f7070696e67=CPuz42fVoxnRVcVQ1x33fa7Yi_bsXs-3QA-gKZCLbXhJE9DcoZX1IkH-jckHAmtY'
		}
      re = json.loads(requests.get(url,headers=headers).text)
      return re

   res = False
   re = get_page(shop_ids[page])
   # print(re)

   # 是否拿到数据，如果有，进行插入操作
   if re.get('menu'):
      menu = re.get('menu')
      res = get_connect(menu, shop_ids[page])
   
   # 是否继续爬
   if res == True and page < len(shop_ids) - 1:
      page = page + 1
      crawler_ele(page)

#数据库的插入操作
def get_connect(menus, shop_id):
   print(shop_id)
   for menu in menus:
      for food in menu.get('foods'):
         info = {}
         restaurant = food
         info['item_id'] = restaurant.get('item_id') #id
         info['name'] = restaurant.get('name') #名字
         info['description'] = restaurant.get('description') #描述
         info['image_path'] = restaurant.get('image_path') #图片路径
         info['month_sales'] = restaurant.get('month_sales') #月售
         info['satisfy_rate'] = restaurant.get('satisfy_rate') #好评率
         specfoods = restaurant.get('specfoods')
         info['price'] = specfoods[0].get('price') #价格
         
         if isExist(info['item_id']):
            print('已经存在')
         else:
            sta = connectdb.exe_update(cur,"insert into final_food(elm_fid, elm_sid, name, description, image_path, elm_month_sales, elm_satisfy_rate, elm_price) values('%s','%s','%s','%s','%s','%f','%f','%f')" % (info['item_id'], shop_id, info['name'], info['description'], info['image_path'], info['month_sales'], info['satisfy_rate'], info['price']))
            if sta == 1:
               print('插入成功')
            else:
               print('插入失败')
   return True
      

def queryShop():
   sta = connectdb.exe_query(cur, 'select elm_sid from final_shop')
   # 去空
   for item in sta:
      if '' in sta:
         sta.remove('')
   return sta

def isExist(fid):
   sta = connectdb.exe_query(cur, 'select * from final_food where elm_fid = "'+fid+'"')
   return len(sta)
   
# 初始化
conn, cur = connectdb.conn_db()
shop_ids = queryShop()

shop_ids = ['E2974532402216861367', 'E1510331724936098152', 'E6139552617649169595', 'E6307634761524182419', 'E10973154398068284688', 'E14612600218770092808', 'E14162466847441764520', 'E1018043893832276933', 'E409887527151416338', 'E13226618366448854581', 'E17830193334368259650', 'E17508925795662539203', 'E5943662264345066439', 'E11663295375700876488', 'E6200574747613562439', 'E1408163753925303626', 'E10327532005397291851', 'E14024697235501204089', 'E9803356968725389333', 'E16906765894021526816', 'E15166300440357677067', 'E8897587375594611602', 'E14441873071755052387', 'E9831324454470022948', 'E7485893069098344904', 'E9569206177034821380','E5746349350834178895', 'E16590470341798810587', 'E2558755149601908620', 'E3344348619285510911', 'E2483444819530989485', 'E7924756213880514966', 'E791455201805287762', 'E6749396430571595903', 'E13367497882264824345', 'E15525585154451491022', 'E8973407388098093684', 'E10993326732692102348', 'E216862783158217713', 'E10777665927424366577', 'E10755849382686470070',
'E1081650591620646094', 'E7387451842027459984', 'E3855069935579715980', 'E11566287391976987750', 'E7928807677208445859','E6674607465351657341', 'E5520969053237159391', 'E8028976139586162865','E5269661659203184565', 'E12347899501370384541','E4886903160335021376', 'E4500806197295030898', 'E12093285384430417275', 'E12300297445048191632', 'E10214953346466124543', 'E38553083877120489', 'E5913215683221788086', 'E17322821161541692778', 'E1371189529887125746', 'E13769107624508684223', 'E9971025298726703207', 'E13550353138201191608', 'E11915538979099664104', 'E11512732102475947291', 'E14456900487631595043', 'E4089332316759447275', 'E3449100064190963427', 'E16650897090916355848']
shop_ids = ['E15126062187090893045']
# 执行主函数
crawler_ele(0)
# 数据库操作
connectdb.exe_commit(cur)    # 注意！！ 一定要记得commit，否则操作成功了，但是并没有添加到数据库中
connectdb.conn_close(conn, cur)