import re

def sqrtInt(n):
   cin = format(n, 'b') #代入した数を2進数化
   lst = []
   s = str(cin)
   if len(s)%2!=0:
      s = "0"+s
   sep = re.split('(..)', s)[1::2]

   #ここから開平法
   result = 0
   subEval = 0
   remained = 0
   for i in range(len(sep)):
      evalution = int(sep[i], 2) + (remained<<2)
      if (subEval<<1)+1 <= evalution:
         result = (result<<1)+1
         remained = evalution - ((subEval<<1)+1)
         subEval = (subEval<<1)+2
      else:
         result = result<<1
         remained = evalution
         subEval = subEval<<1

   return result

def isSqr(n):
   if (n%12==0 or n%12==1 or n%12==4 or n%12==9):
      cin = format(n, 'b') #代入した数を2進数化
      lst = []
      s = str(cin)
      if len(s)%2!=0:
         s = "0"+s
      sep = re.split('(..)', s)[1::2]

      #ここから開平法
      subEval = 0
      remained = 0
      for i in range(len(sep)):
         evalution = int(sep[i], 2) + (remained<<2)
         if (subEval<<1)+1 <= evalution:
            remained = evalution - ((subEval<<1)+1)
            subEval = (subEval<<1)+2
         else:
            remained = evalution
            subEval = subEval<<1
            
      return remained == 0
   return False
