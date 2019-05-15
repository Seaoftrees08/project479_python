import time
import sqrtlib

try:
   n = int(input(">> "))
   start = time.time()

   result = 2
   if n%2!=0:
      result += 1
      r = sqrtlib.sqrtInt(n)+1
      while result<r and n%result!=0:
         result += 2

   print("result: " + str(result) + " " + str(n/result))
   print("time: " + str(time.time()-start))

except ValueError:
   print("You can input only number.")