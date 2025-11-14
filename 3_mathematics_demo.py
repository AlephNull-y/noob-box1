#这是字符串"6"
#这是整数6
#这是浮点数6.0
1+2-3*4/5**6//7%8  # 输出 3.0
#这是字符串 --- IGNORE ---
import math
print(math.pi)  # 输出圆周率
print(math.e)   # 输出自然常数
print(math.sqrt(16))  # 输出16的平方根
print(math.pow(2, 3))  # 输出2的3次方
print(math.sin(math.pi / 2))  # 输出sin(π/2)
print(math.log(math.e))  # 输出自然对数ln(e)
print(math.factorial(5))  # 输出5的阶乘
print(math.gcd(48, 18))  # 输出48和18的最大公约数
#  --- IGNORE ---
#一元二次方程求根公式演示
a = 1
b = -3
c = 2
discriminant = b**2 - 4*a*c
if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("方程的根为：", root1, "和", root2)
else:
    print("方程无实数根")
#  --- IGNORE ---
#eg:-x**2-2x+3=0
a = -1
b = -2 
c = 3
#-b + (b ** 2 - 4 * a * c)**0.5/(2*a)
#(-b - math.sqrt(b**2-4*a*c))/(2 * a)
x=(-b - math.sqrt(b**2-4*a*c))/(2 * a)
print("方程的根为：", x)