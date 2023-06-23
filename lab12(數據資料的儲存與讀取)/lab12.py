#台南市公有免費停車場
#https://data.gov.tw/dataset/102775
import pymysql
import requests
r = requests.get('https://citypark.tainan.gov.tw/App/parking.ashx?verCode=5177E3481D&type=1&ftype=1&exportTo=2')#得到這個網址的資料
list1=r.json()
types=[]
nums=[]
names=[]
address=[]
for i in range(0,10):
    dict0=list1[i]
    types.append(dict0['停車場型態'])
    nums.append(dict0['停車場代碼'])
    names.append(dict0['停車場名稱'])
    address.append(dict0['停車場地址'])

db_settings = {# 資料庫設定
    "host": "localhost",
    "port": 3306,
    "user": "E94116075",
    "password": "921123Aa",
    "db": "wordpress",
    "charset": "utf8"
}
conn = pymysql.connect(**db_settings)#連線
    
with conn.cursor() as cursor:# 建立Cursor物件
        
    command = "INSERT INTO `臺南市公有免費停車場`(`停車場型態`,`停車場代碼`,`停車場名稱`,`停車場地址`)VALUES(%s, %s, %s,%s)"# 新增資料SQL語法
    for i in range(0,10) :
        cursor.execute(
            command, (types[i], nums[i],names[i],address[i]))
        
    conn.commit()# 儲存變更
conn.close()#關閉
