
int(input())

Map =[
   [1,2,3,4,5],
   [1,2,3,4,5],
   [1,2,3,4,5],
   [1,2,3,4,5],
   [1,2,3,4,5]
]

customerDatas = [[1,1],[2,3],[4,5]]

for y in range(len(Map)):
   xDatas =Map[y]
   row = []
   for x in xDatas:
      hasCustomer = "O";
      for customerData in customerDatas:
         if([x,y+1] == customerData):
            hasCustomer = "X";
      row.append(hasCustomer)
   print(row)
