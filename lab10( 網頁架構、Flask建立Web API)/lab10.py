# 複製就對了
from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# web server 路由設定
# 若有get request傳送到 / ，就會執行他下面的這個function，function名稱隨意，但不可重複
@app.route('/',methods=['GET'])
def root():
    return 'ok' # 發送response body 為 ok

@app.route('/key_list',methods=['GET'])
def root3():
    key1=list(dict1.keys())
    return str(key1)
# 設定路由為/set
# 使用 request.form 來接收body的資料，接著用to_dict()這個function來轉成python的dict格式，就可以使用這個資料了
@app.route('/set',methods=['POST'])
def root2(): 
    data =request.form.to_dict()
    value1=list(data.values())
    b=value1[0] in dict1   
    if b==False:
        dict1[value1[0]]=value1[1]
        return 'set success'
    else:
        return 'key exist'

@app.route('/get_value/<key>',methods=['GET'])
def root4(key):
    print(key)
    b=key in dict1
    if b==False:
        return 'key not found'
    else:
        key=dict1.setdefault(key)
        return key # 發送response body 為 ok


@app.route('/update_value',methods=['POST'])
def root5():
    data =request.form.to_dict()
    value1=list(data.values())
    b=value1[0] in dict1
    if b==False:
        return 'key doesn\'t exist'
    else:
        dict1[value1[0]]=value1[1]
        return 'update success' # 發送response body 為 ok

@app.route('/delete/<key>',methods=['GET'])
def root6(key):
    b=key in dict1
    if b==False:
        return 'key not found'
    else:
        del dict1[key]
        return 'delete success' # 發送response body 為 ok



     # 發送response body 為 ok

# 將webserve，監聽任意來源ip，port開在3000，開啟debug模式
# debug模式代表，每次檔案更新後，webserver會自動重啟，不需要手動重啟
dict1={}
app.run(host="0.0.0.0", port=3000, debug=True)

