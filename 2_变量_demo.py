#变量练习的小纠错
#my_love = 123456789
#print("拨打：" + my_love)
#报错原因：此时my_love不是字符串，python不允许字符串与非字符串拼接
my_love = 123456789
print("拨打：" + str(my_love))
my_love = "123456789" 
print("拨打：" + my_love)

greet_english="hello"
greet_chinese="你好"
greet=greet_chinese
print(greet+" name")