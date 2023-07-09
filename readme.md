# lab簡介
lab07以前主要為Python基本操作，以後為應用，如資料視覺化、socket programming、AI手寫數字辨識等
* lab02
  - 建立一個名為lab02的資料夾，內有一個檔案名稱為學號的檔案，內容隨意但不可空白
* lab03
  - 利用input/output if/else 判斷奇偶數並輸出學號  
* lab04
  - 利用for, input()輸入學生的成績，並且利用list儲存  
    計算平均成績請使用迴圈  
* lab05  
  - 建立一個名稱為「dict0」的字典，其資料內容如下。

    | 鍵(key) |	值(value) |
    | ---- | ---- |  
    | index	| 國文, 英文, 數學, 自然, 社會  |  
    | StuA	| 50, 60, 70, 80, 90 |  
    | StuB	| 57, 86, 73, 82, 43 |   
    | StuC	| 97, 96, 86, 97, 83 |
    
  - 將同一個key之多個value以list方式儲存。  
    輸出整個dict0字典。  
    計算出每個學生的平均成績(StuA, StuB, StuC)。  
    計算出每個科目的平均成績(國文, 英文, 數學, 自然, 社會)。    
* lab06  
  - 使用輾轉相除法，為兩個數字求出最大公因數，並輸出：「num1和num2的最大公因數=num3」，若兩個數字互質，則輸出：「num1和num2互質。」需自己定義一個函式gcd  
* lab06_plus  
  - 使用random module，投擲1000000次骰子(骰子點數為1~6)，列出每個點數被骰到的機率(Prob)。(精準至小數點後第2位)。  
* lab07
  - 請建立一個名為Animals的class，以及兩個名為Dogs跟Cats的子類別，已知Dogs跟Cats都屬於Animals的一種，請依以下敘述建立最適合的class。
    已知Animals具有以下attribute：
    weight：體重  
    mood：心情  
    已知Animals具有以下method：    
    feed()：吃飯  
    walk()：散步  
    bath()：洗澡  
    分別建立一個dog和cat的物件，初始值如下：  
    | object | Animals weight	| mood |
      | ---- | ---- | ---- |      
    | Dogs	| 4.8 kg | 65 |  
    | Cats	| 8.2 kg | 60 |
  
    dog = Dogs(4.8, 65)  
    cat = Cats(8.2, 60)  
    當我們帶Animals去吃飯(feed) 時，會影響到Animals的weight和mood，如下表所示：  
    | Aniamls	| weight | mood |
       | ---- | ---- | ---- |        
    | Dogs	| +0.2 kg | 	+1 |    
    | Cats	| +0.1 kg	| +1 |
    
    當我們帶Animals去散步(walk) 時，會影響到Animals的weight和mood，如下表所示：  
   | Aniamls	| weight | mood |  
   | ---- | ---- | ---- |       
   |  Dogs	| -0.2 kg	| +2 |   
  | Cats	| -0.1 kg	| -1 |

    當我們帶Animals去洗澡(bath) 時，會影響到Animals的mood，如下表所示：  
    | Aniamls	| weight | mood |
       | ---- | ---- | ---- |      
    | Dogs	| 不影響	 | -2 |    
    | Cats	| 不影響	 | -2 |
    
    Quesion:  
    假設這一個月，Animals吃飯、散步、洗澡的次數如下表所示， 請輸出dog和cat現在的體重和心情分別為何。  
    | object	| n_feed	| n_walk | n_bath |
       | ---- | ---- | ---- | ---- |          
    | dog	| 18 | 	10 |	4 |    
    | cat| 40| 7| 1 |
    
* lab08
  - 讀取當前工作目錄並存成list，print在終端機裡，然後將裡面的元素一行一行寫入文字檔
  - 讀取 ‘/home/學號’ 目錄下所有檔案和資料夾，print在終端機裡，然後將裡面的元素一行一行寫入文字檔
（兩題寫入同一個文字檔、兩題之間用一行空白隔開，請使用linesep跟sep）
* lab09
  1. Linux Networking Commands (15%)
  - 測試是否可以上網(從樹莓派輸入指令)
  - 查看隨便一個網址(e.g. google.com, apple.com, etc.)的ip
  - 查看到那個網頁的路徑
  2. RaspAP (15%)
    - 更改Hotspot名稱&密碼(要Save settings, Restart hotspot)，安全起見不要設定的太簡單，但自己要能記住。
    - 測試是否可以上網(從電腦輸入指令)
    - 將手機連上AP，測試是否可以連到手機
    - 給電腦設定一個固定IP:10.3.141.xx(與原本DHCP配發的IP相同即可)
    ，查看從此電腦(10.3.141.xx)到google.com的路徑為何
  3. Socket programming (70%, 要先完成第2題才會算分)
    - 請寫一個TCP Socket，功能：Server接收到Client傳來的訊息後，會回覆一模一樣的訊息給Client
* lab09_plus
  - 讓Server可以同時服務多個Client(上述Server同時間只能服務一個Client)
* lab10
  - 完成一個web server，並且具有以下API
  
|api名稱	|method	|傳入資料	|功能|
| :-----| :---- | :----| :----|
| /GET	| 無 |  | 接收get request後 回傳ok (一定要是’ok’！不能是OK, okay或是多任何空格)|  
| /set	| POST		|  | 新增一個 key-value pair 並回傳’set success’，若key已存在 則回傳’key exist’ |  
|/key_list	|GET	|無|	回傳所有存在的 key (記得要轉為str格式)|
|/get_value/{key}	|GET|	無|	回傳指定的 key 的資訊，若找不到就回傳’key not found’|  
|/update_value|	POST		| |更新指定的 key 的資訊並回傳’update success’，若 key 不存在 則回傳’key does not exist’|  
| /delete/{key}|	GET|	無	|刪除指定的 key 的資訊並回傳’delete success’，若找不到就回傳’key not found’|  
* lab10_plus
  - 將所有輸入的 key-value pair儲存在本地的資料庫，不可存在ram中(即不可使用任何資料型態的變數來儲存)，方法隨意，可以用txt檔、資料庫等，當web server重新啟動時，可以讀取到過去建立的 key-value pair
(須處理掉多餘的換行、空格等多餘字元)
* lab11
  - 假設有 N件工作 (Job)要處理，手邊有 N個人 (Agent)可以指派，每個人必須處       理任意一件工作，每個工作也必須被任意一個人處理，請問如何指派可使得總成本最低？
  - 請使用input.json作為測資，形式為 dictionary，key 為題號，value 為測試的 input
  - https://drive.google.com/file/d/1-4GXpX-f8nPVIarpjvgYaJLWRuVzoQcI/view
* lab12
  - 安裝PyMySQL
  - 請至政府資料開放平臺(https://data.gov.tw/) 選擇一個、資料集
選擇類別、選擇資料集、點選JSON
  - 用phpMyAdmin在資料庫中建立新的資料表，並新增至少四個欄位，使用PyMySQL與資料庫做溝通，最後根據API新增10筆以上的資料
* lab13
  - 下載Temperature.txt到lab13資料夾中，與lab13.py一樣路徑，請搜尋python read txt file來讀取Temperature.txt
  - 將歷年的台南氣溫資料用plt.plot()繪製成如下圖，儲存圖片命名為 lab13_01.png
hint: 可以自己建立一個年份的list，利用for迴圈可以提高撰寫效率
  - 分別計算每個月份每年的氣溫平均值，把12個月份分別的的氣溫平均值繪製成一張表
計算每個月分氣溫的總平均值(全部的平均)，在圖表上繪製一條水平虛線，並且標示總平均值的數字在須線上，儲存圖片命名為 lab13_02.png
  - 將前面兩張圖片使用subplot(1,2,x)畫在同一張圖片上，儲存圖片命名為 lab13_03.png
* lab15  
  https://hackmd.io/@MCAS/Student_Lab15
  
