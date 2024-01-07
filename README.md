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
>python -m venv my_env 建虛擬機
>my_env\Scripts\activate #進入虛擬機環境
>(my_env)>pip install -r requirements.txt #一次安裝所有套件
>(my_env)>deactivate #退出虛擬機環境

## 啟動server
>進入虛擬機環境
>python manage.py migrate #看起來只需要下第一次 好像是串DB
>python manage.py runserver #啟動server 預設為http://127.0.0.1:8000/
