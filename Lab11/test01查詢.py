import _sqlite3
#建立連線
con = _sqlite3.connect(r'/Applications/MyDB.db')
#取得游標
c = con.cursor()
#設定所需要執行的ＳＱＬ語句
c.execute('SELECT CustomerID, Customername FROM customers')
#提交ＳＱＬ語句
con.commit()
#使用for迴圈逐筆讀取 提出資料
for row in c:
    print(row)
    CustomerID, Customername = row
    print(CustomerID)
    print(Customername)

con.close()