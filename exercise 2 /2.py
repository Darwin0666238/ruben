import math
import numexpr as me 

x=ne.evaluate(input("ввудите переменную х  :"))
y=float(input("введите переменную  у  :"))
z=float(input("введитие переменную z  :"))
s=math.sqrt(10*(math.pow(x,1/3)+x**(y+2)))*(math.asin(z)**2-abs(x-y))

print("s={0:.4f}".format(s))
