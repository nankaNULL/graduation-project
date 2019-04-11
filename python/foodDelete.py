# coding=utf-8
import json
import connectdb

# 店铺列表
def main():
  deleteIds = getDeleteIds()
  delete_connect(deleteIds)

def getDeleteIds():
  deleteIds = []
  fids = connectdb.exe_query(cur,"select elm_fid from final_food")
  for fid in fids:
    if fid:
      count = 0
      for f in fids:
        if f == fid:
          count = count + 1
      if count > 1:
        deleteIds.append(fid)
  return deleteIds

def delete_connect(deleteIds):
  for i in range(len(deleteIds)):
    sta = connectdb.exe_update(cur,"delete from final_food where elm_fid="+deleteIds[i])
    # if sta == 1:
    #   print("删除成功")
    # else:
    #   print("删除失败")
    

conn, cur = connectdb.conn_db()
main()
connectdb.exe_commit(cur)    # 注意！！ 一定要记得commit，否则操作成功了，但是并没有添加到数据库中
connectdb.conn_close(conn, cur)
