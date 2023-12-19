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

## 虛擬機
>python -m venv my_env #建my_env
>my_env\Scripts\activate #進入虛擬機環境
>(my_env)>deactivate #退出虛擬機環境
### 例外情況
如果遇到 my_env\Scripts\activate : 因為這個系統上已停用指令碼執行，所以無法載入 D:\...\stock-decision-support-system-backend\
>Set-ExecutionPolicy RemoteSigned #下這個


## 啟動server
>進入虛擬機環境
>python manage.py migrate #看起來只需要下第一次
>python manage.py runserver #啟動server 預設為http://127.0.0.1:8000/

