import time
import time
import sqrtlib

#main 250,000 trials/sec
try:
   n = int(input(">> "))
   y = 1

   start = time.time()  
   if n%2!=0:
      x = sqrtlib.sqrtInt(n)+1
      while not sqrtlib.isSqr(x*x-n):
         x += 1
      y = sqrtlib.sqrtInt(x*x - n)
      print("result: " + str(x-y) + " " + str(x+y))
   else:
      print("result: 2 " + str(n>>1))
   print("time: " + str(time.time() - start))
   print("Number of trials: " + str(y))

except ValueError:
   print("You can input only number.")