import _sqlite3
#建立連線
con = _sqlite3.connect(r'/Applications/MyDB.db')
#取得游標
c = con.cursor()

cus_id = input('請輸入欲查詢顧客id')

#設定所需要執行的ＳＱＬ語句
query = 'SELECT CustomerID, Customername FROM customers WHERE CustomerID={}'.format(cus_id)
print(query)
c.execute(query)
#查詢customers,只顯示customerid and customername

#提交ＳＱＬ語句
con.commit()
s = 0
#使用for迴圈逐筆讀取 提出資料
for row in c:  #row 列(exel 試算表)
    print(row) #row 為 tuple 唯獨的串列
    CustomerID, Customername = row
    print(CustomerID)
    print(Customername)
    s += 1
print('s = ',s)
if s == 0:
    print('查無此筆資料')
con.close()