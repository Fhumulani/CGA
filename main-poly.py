import CGA
import Sphere
import time
import matplotlib.pyplot as plt
import numpy as np

now = time.time()

gen =10000
M = 50
lb = [26.]
ub = [27.]
Pc = 0.95;
Pm = 0.5;
Er = 0.2;
N = len(lb)

s = [1,5,5,5,6,1]

b,c = CGA.CGA(gen,lb,ub,M,N,Sphere,Pc,Pm,Er,s)
print("we are done")


x = np.arange(-10,10)
y =  s[0]*x**5 - s[1]*x**4 + s[2]*x**3 + s[3]*x**2 - s[4]*x  - s[5]
y1 = b[0]*x**5 - b[1]*x**4 + b[2]*x**3 + b[3]*x**2 - b[4]*x  - b[5]

print(time.time()-now)
for i in range(1,5):
   try:
      y2 = c[-i*10][0]*x**5 + c[-i*10][1]*x**4 + c[-i*10][2]*x**3 + c[-i*10][3]*x**2 + c[-i*10][4] * x + c[-i*10][5]
      plt.plot(x, y2, "v", label="generation {0}".format(i))
   except:
      y2 = c[len(c) - 1][0]*x**5 + c[len(c) - 1][1]*x**4 + c[len(c) - 1][2]*x**3 + c[len(c) - 1][3]*x**2
      +c[len(c) - 1][4]*x + c[len(c) - 1][5]
      plt.plot(x, y2, "*", label="generation {0}".format(len(c) + 10))
      # plt.show()
      break
#   plt.xlabel("Generation no#")
#   plt.ylabel("fitness")

plt.plot(x,y,"-o",label="poly")
plt.plot(x,y1,"*",label="best fit",markersize=1)
plt.legend(loc="best")
plt.savefig("GA.png")
plt.show()





