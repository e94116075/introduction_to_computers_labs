# lab簡介
lab07以前主要為Python基本操作，以後為應用，如資料視覺化、socket programming、AI手寫數字辨識等
* lab03
  - 利用input/output if/else 判斷奇偶數並輸出學號  
* lab04
  - 利用for, input()輸入學生的成績，並且利用list儲存  
    計算平均成績請使用迴圈  
* lab05  
  - 建立一個名稱為「dict0」的字典，其資料內容如下。  
    鍵(key)	值(value)  
    index	國文, 英文, 數學, 自然, 社會  
    StuA	50, 60, 70, 80, 90  
    StuB	57, 86, 73, 82, 43  
    StuC	97, 96, 86, 97, 83  
    將同一個key之多個value以list方式儲存。  
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
    object	Animals	weight	mood  
    dog	Dogs	4.8 kg	65  
    cat	Cats	8.2 kg	60  
    dog = Dogs(4.8, 65)  
    cat = Cats(8.2, 60)  
    當我們帶Animals去吃飯(feed) 時，會影響到Animals的weight和mood，如下表所示：  
    Aniamls	weight	mood  
    Dogs	+0.2 kg	+1  
    Cats	+0.1 kg	+1  
    當我們帶Animals去散步(walk) 時，會影響到Animals的weight和mood，如下表所示：  
    Aniamls	weight	mood  
    Dogs	-0.2 kg	+2  
    Cats	-0.1 kg	-1  
    當我們帶Animals去洗澡(bath) 時，會影響到Animals的mood，如下表所示：  
    Aniaml	weight	mood  
    Dogs	不影響	-2  
    Cats	不影響	-2  
    Quesion:  
    假設這一個月，Animals吃飯、散步、洗澡的次數如下表所示， 請輸出dog和cat現在的體重和心情分別為何。  
    object	n_feed	n_walk	n_bath  
    dog	18	10	4  
    cat	40	7	1  
* lab08
  - 讀取當前工作目錄並存成list，print在終端機裡，然後將裡面的元素一行一行寫入文字檔
讀取 ‘/home/學號’ 目錄下所有檔案和資料夾，print在終端機裡，然後將裡面的元素一行一行寫入文字檔
注意事項：

兩題寫入同一個文字檔
兩題之間用一行空白隔開
請使用linesep跟sep
* lab09  
