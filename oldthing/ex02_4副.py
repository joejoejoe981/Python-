#[[1,2,3],[1,2,3],[1,2,3]]

def ShowSitMap(sitMap,customerData):
   for rowIndex in range(len(sitMap)):
      row =sitMap[rowIndex]
      if (row == customerData).all():
       return True;
      else: return False;

