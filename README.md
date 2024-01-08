# stock-decision-support-system-backend
pull專案前建議將fork資料夾於防毒軟體設定例外
在install django時防毒有跳出來掃描過

## 專案成員
| 分群 | 名稱 | 學號 |
| -------- | -------- | -------- |
| 後端     | 歐     | 11046003     |
| 後端     | 朱     | 11046013     |
| 全端     | 彭     | 11046029     |
| 前端     | 童     | 11046002     |
| 前端     | 尤     | 11046033     |

## 環境變數
加入這兩個到系統變數的"path"裡面
<div style="color: red;">請使用3.11以下的python版本 永豐金不支援312==</div>
C:\Users\user\AppData\Local\Programs\Python\你的版本\Scripts
C:\Users\user\AppData\Local\Programs\Python\你的版本
看不懂可以google python環境變數

## 虛擬機
>python -m venv my_env 建虛擬機 注意版本
>my_env\Scripts\activate #進入虛擬機環境 
>(my_env)>pip install -r requirements.txt #一次安裝所有套件
>(my_env)>deactivate #退出虛擬機環境
>python manage.py test backend.tests #測試backend裡面的tests檔案

## 啟動server
>進入虛擬機環境
>python manage.py migrate #看起來只需要下第一次 好像是串DB
>python manage.py runserver #啟動server 預設為http://127.0.0.1:8000/

## 串金流
模擬模式可以用的api可以參考官方文件 https://sinotrade.github.io/zh_TW/tutor/simulation/
要用永豐金api都得登入 記得開模擬模式 帳密我丟群組 不要上傳到github gitigrone我設定ㄌ 應該不會有人亂丟上去吧...
其他看起來比較有用的我都有在backend/test.py測過了 可以參考 剩的都到官方文件看
```python
import shioaji as sj
import yaml

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

api = sj.Shioaji(simulation=True)  # 模擬模式
api.login(
    api_key=config["shioaji"]["api_key"],
    secret_key=config["shioaji"]["secret_key"],
)
```
        