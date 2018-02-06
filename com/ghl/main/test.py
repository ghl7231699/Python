# -*- coding: UTF-8 -*-
import calendar
import time
import math
import os

print "this is my first python demo:Hello World"
if True:
    print "True"
else:
    print "False"

counter = "LiLi"  # 字符串
miles = 1000.0  # 浮点型
xinle = 1000  # 整形

print counter
print miles
print xinle

a = "what for you "
b = 'what for you '
print "a==" + a
print "b==" + b
# 单行注释的使用
# temp=input("you say 爱:")
# guess=int(temp)
# if guess==8:
# 	print "love"
# else:
# 	print 'you are wrong'
# 多个变量赋值
a = b = c = d = 1
print a + b + c + d
# Python字符串
s = "iloveyoumycountry"
print s[1:5]  # 输出字符串中第2个至第五个之间的字符串
print (s[0:8] + "\n") * 2  # 输出第一个至第八个之间的字符创 输出两次
print s[1:]  # 输出从第二个位置开始到结束的字符串
print s[1:5] + "country"  # 输出连接的字符串

# 列表
fruits = ["banana", "apple", "melon"]
ball = ["basketball", "football", "badminton"]
print fruits  # 输出完整列表
print fruits[0]  # 输出列表的第一个元素
print fruits[0:1]  # 输出第一个至第二个元素 但不包括第三个
print fruits[1:]  # 输出从第二个开始至列表末尾的所有元素
print ball * 2  # 输出列表两次
print fruits + ball
# 元组
tuple = (1, 100.1, 2.23, 'what', 'this is tuple')
tinytuple = (123, "john")

print tuple  # 输出完整元组
print tuple[0]  # 输出元组的第一个元素
print tuple[1:4]  # 输出第二个至第五个元素
print tuple[1:]  # 输出第二个元素至元组末尾的所有元素
print tinytuple * 2  # 输出元组两次
print tuple + tinytuple  # 输出组合的元组

# 字典（类似于java中的map）#
diction = {}
diction['name'] = "joke"
diction[1] = 8.88
tinydiction = {'one': "this is one", 2: 6.66, 'code': "myCode"}

print diction['name']  # 输出key为one 的值
print diction[1]  # 输出key 为1的值
print tinydiction  # 输出完整的字典
print tinydiction.keys()  # 输出所有key
print tinydiction.values()  # 输出所有值
# 数据类型转换
print hex(4)  # 将一个整数转换成十六进制字符串
print oct(8)  # 将一个整数转换为八进制字符串
print unichr(99)  # 将一个整数转换为Unicode字符
# 算数运算符
a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为：", c
c = a - b
print "2 - c 的值为：", c
c = a * b
print "3 - c 的值为：", c
c = a / b
print "4 - c 的值为：", c
c = a % b
print "5 - c 的值为：", c
# 修改变量a、b、c
a = 2
b = 3
c = a ** b
print "6 - c 的值为：", c
a = 10
b = 6
c = a // b
print "7 - c 的值为：", c

# 比较运算符
if a == b:
    print "1 - a 等于 b"
else:
    print "1 -  a 不等于 b"

if a != b:
    print "2 - a 不等于 b"
else:
    print "2 -  a 等于 b"

if a <> b:  # 类似!=
    print "3 - a 不等于 b"
else:
    print "3 -  a 等于 b"

if a < b:
    print "4 - a 小于 b"
else:
    print "4 -  a 大于等于 b"

if a > b:
    print "5 - a 大于 b"
else:
    print "5 -  a 小于等于 b"

# 修改变量 a 和 b 的值
a = 10
b = 20
if a <= b:
    print "6 -  a 小于等于 b"
else:
    print "6 - a 大于 b"
if b <= a:
    print "7 -  a 大于等于 b"
else:
    print "6 - a 小于 b"

# 赋值运算符
a = 2
b = 3
c = 0
c = a + b
print "1 - c 的值为：", c
c += a
print "2 - c 的值为：", c
c *= a
print "3 - c 的值为：", c
c /= a
print "4 - c 的值为：", c
c %= a
print "5 - c 的值为：", c
c **= a
print "6 - c 的值为：", c
c //= a
print "7 - c 的值为：", c

# 位运算符
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b
print "1 - c 的值为：", c
c = a | b
print "2 - c 的值为：", c
c = a ^ b
print "3 - c 的值为：", c
c = ~a
print "4 - c 的值为：", c
c = a << 2
print "5 - c 的值为：", c
c = a >> 2
print "6 - c 的值为：", c
# 成员运算符
a = 10
b = 20
list11 = [1, 2, 3, 4, 5, 6]

if a in list11:
    print "1 - 变量 a 在给定的列表中"
else:
    print "1 - 变量 a 不再给定的列表中"

if b not in list11:
    print "2 - 变量 b 不在给定的列表中"
else:
    print "2 - 变量 b 在给定的列表中"

a = 2
if a in list11:
    print "3 - 变量 a 在给定的列表中"
else:
    print "3 - 变量 a 不再给定的列表中"

# 身份运算符
a = 20
b = 20
if a is b:
    print "1 - a 和 b 有相同的标识"
else:
    print "1 - a 和 b 没有相同的标识"
if a is not b:
    print "2 - a 和 b 没有相同的标识"
else:
    print "2 - a 和 b 有相同的标识"
b = 10
if a is b:
    print "3 - a 和 b 有相同的标识"
else:
    print "3 - a 和 b 没有相同的标识"
if a is not b:
    print "4 - a 和 b 没有相同的标识"
else:
    print "4 - a 和 b 有相同的标识"
a = [1, 2, 3]
b = a
print b is a
print b == a
b = a[:]
print b
print b is a
print b == a
# 运算符优先级
a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d
print "(a + b）* c / d 运算结果为：", e

e = ((a + b) * c) / d
print "（(a + b）* c) / d 运算结果为：", e

e = (a + b) * (c / d)
print "（(a + b) * (c / d) 运算结果为：", e

e = a + (b * c) / d;  # 20 + (150/5)
print "a + (b * c) / d 运算结果为：", e

# 例1： if的基本用法
flag = False
name = 'joke'
if name == 'python':
    flag = True
    print 'welcome to python'
else:
    print name

num = 0
if num == 3:
    print 'Hello'
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num <= 0:
    print "error"
else:
    print 'boss'
# 多个判断语句
num = 9
if num > 0 or num <= 10:
    print "you are right"
num = 10
if num < 0 or num > 10:
    print "you are right"
else:
    print 'you are wrong'

num = 8
if (num >= 0) and num <= 5 or (num >= 10) and num <= 15:
    print 'you are right'
else:
    print 'undefine'

# 简单的语句组
var = 100

if var == 100: print "变量 var 的值为100"
print "刚好遇见你"


# 一个简单的条件循环语句实现汉诺塔问题
def my_print(args):
    print args


def move(n, a, b, c):
    my_print((a, '--->', c)) if n == 1 else (move(n - 1, a, c, b) or move(1, a, b, c) or move(n - 1, b, a, c))


move(3, 'a', 'b', 'c')

# 循环语句
# while循环
count = 0
while count < 9:
    print 'this count is ', count
    count = count + 1

print 'over'

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print i  # 输出双数2、4、6、8、10

j = 1
while 1:  # 循环条件为1必定成立
    print j  # 输出1~10
    j += 1
    if j > 10:  # 当i大于10时跳出循环
        break
        # #无限循环
# var = 1
# while var == 1:
# 	num = raw_input("Enter a number :")
# 	print "You entered :",num
# print "Bye Bye"
# 循环使用else语句
count = 0
while count < 5:
    print count, "is less than 5"
    count += 1
else:
    print count, 'is large than 5'

# for循环
for letter in 'Python':
    print '当前字母 ：', letter
    break

fruits = ['apple', 'banana', 'mogo', 'peach', 'melon']

for fruit in fruits:
    print '当前水果 ：', fruit

# 通过序列索引迭代
for index in range(len(fruits)):
    print '当前水果 ：', fruits[index], 'do you like it?'
# 循环使用else语句
for num in range(10, 20):
    for i in range(2, num):
        if num % 2 == 0:
            j = num / i
            print '此时的j为：', j
            print '此时的i为：', i
            print '%d 等于 %d * %d' % (num, i, j)
            break
            # else:
            # 	print '此时的i为：',i
    else:
        print num, '是一个质数'
# 使用list.append()模块对质数进行输出
prime = []
for num in range(2, 100):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        prime.append(num)
print prime
# 冒泡排序
array = [1, 8, 9, 3, 7, 4, 6, 5, 10]
for i in range(len(array)):
    for j in range(i + 1):
        if array[i] < array[j]:
            array[i], array[j] = array[j], array[i]
print array

# 输出菱形
# width = int()
# width = int(raw_input('输入对角线长度： '))
# for row in range(width + 1):
#     for col in range(width + 1):
#         if ((abs(row - width/2) + abs(col - width/2)) == width/2):
#             print "*",
#         else:
#             print " ",
#     print " "
# 循环嵌套
i = 2
while i < 100:
    j = 2
    while j <= (i / j):
        if not (i % j):
            break
        j = j + 1
    if j > i / j:
        print i, '是素数'
    i += 1
# break语句
for letter in 'Python':
    if letter == 'h':
        break
    print '当前字母为', letter

var = 10
while var > 0:
    print '当前变量值为：', var
    var = var - 1
    if var == 5:
        break
# continue语句
for letter in 'Python':
    if letter == 'h':
        print '中止本次循环', letter
        continue
    print '当前字母为', letter
# 打印0-100之间的奇数
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print n
# pass
for letter in 'Python':
    if letter == 'h':
        pass
    print '当前字母 :', letter

# 字符串格式化符号
print "My name is %s and weight is %d kg" % ("libin", 80)
# 三引号的使用
hi = '''hi come here'''
print hi

# list
list1 = ['physics', 'chemistry', 2000, 1998, 2018]
list2 = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
# 列表截取
print list1[0]
print list2[0]

# 列表组合
print list1 + list2

# 获取列表长度

print 'list1的长度为', len(list1)
print 'list2的长度为', len(list2)

# 删除列表元素
del list1[0]
print '删除后的数组为：', list1

# 元素是否存在于列表中

if 'chemistry' in list1:
    print '数组中存在----->True'
else:
    print '数组中没有这个数据'

# 迭代
for i in list1:
    print 'this one is ', i
# 比较两个列表的元素
print '比较结果是', cmp(list1, list2)

# 列表的最大值、最小值
print max(list1)
print min(list2)

# 将元组转换为列表
list3 = list(tuple)
print '转化后的结果为：', list3

# 在列表末尾添加新的元素

list1.append('joke')
print '添加后的结果为', list1
# 在列表末尾一次性追加另一个序列中的多个值

list3.extend(list1)
print list3

# 统计某个元素在列表中出现的次数
print list3.count(1)

# 从列表中找出某个值第一个匹配项的索引位置
list2.append(2017)
print 'list2为', list2
positon = list2.index(2017)
print '索引位置为', positon
# 将对象插入列表

list1.insert(3, 'world')
print list1
# 移除列表中的一个元素(默认最后一个元素)，并返回该元素的值
print list2.pop(0)
print list2

# 移除列表中某个值得第一个匹配项
print list2.remove(2017)
print list2

# 反向列表中的元素
list3.reverse()
print list3
# 对原列表进行排序
list2.sort()
print list2

# 元组
t1 = (1, 2, 3, 4, 'LiLi')
t2 = (5, 6, 7, 8, 'yaya', 'hehe')

# 字典
dict1 = {'a': [1, 2]}
dict2 = {'a': {'c': 10}}
print dict1['a'][1]
print dict2['a']['c']

# 日期和时间
ticks = time.time()
print '当前时间戳为：', ticks
# 获取当前时间
localtime = time.localtime(ticks)
print '本地时间为:', localtime
# 获取格式化时间
now = time.asctime(localtime)
print '现在的时间为', now
# 格式化时间
# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
# 将格式字符串转换为时间戳
a = "Fri Feb  2 10:27:36 2018"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
# 获取某月日历
cal = calendar.month(2018, 2)
print '下面输出2018年2月份的日历：'
print cal
print calendar.calendar(2018)
print calendar.monthcalendar(2018, 2)


# 函数
# 定义一个函数
def functionname(parameters):
    """打印输入的字符串"""
    print parameters
    return parameters


p = functionname("you cloud't love your country")
print p
functionname("Because she's like your mother")


# 参数传递
# 传不可变对象实例
def changeint(aaa):
    aaa = 10
    print aaa


b = 1
changeint(b)
print b


# 传递可变参数
def changelist(l):
    """"修改传入的列表"""
    l.append([1, 2, 'what'])
    l[2] = 'why'
    print '函数内列表的值为：', l


l = [1, 2, 6]
changelist(l)
print '函数外列表的值为：', l


# 参数
# 1 必备参数
# 2 关键字参数
def printme(str):
    print str
    return


printme(str='hello world')


def printinfo(name, age):
    print "name", name
    print "age", age
    return


printinfo(age=100, name="Mike")


# 3 缺省参数
def printmessage(name, age=28):
    print "name", name
    print "age", age
    return


printmessage(age=29, name='Joke')
printmessage('Jiajia')


# 4 不定长参数
def printmulti(arg1, *var):
    print '输出'
    print arg1
    for values in var:
        if values > 0 and values < 10:
            print '不定参数为', values
        else:
            print 'Sorry there is nothing you want here'
            break


printmulti(10)
printmulti('start', 3, 14, 5, 11, 12)

# 5 匿名函数
sum = lambda arg1, arg2, arg3: arg1 - arg2 + arg3
print '结果是', sum(10, 20, 30)
print '结果是', sum(1, 1, 0)


# 6 return语句
def sum(arg1, arg2):
    total = arg1 + arg2
    return total


total = sum(10, 20)
print '函数返回值为', total
# 命名空间和作用域
money = 1000


def addmoney():
    global money
    money = money + 100


print money
addmoney()
print money

# dir 函数
content = dir(math)
print content

# #input函数
# str = input("请输入：")
# print "你输入的内容是",str
# 文件操作
file = open("test.txt", "wb")
print "文件名", file.name
print "是否已关闭", file.closed
print "访问模式", file.mode
print "末尾是否强制加空格", file.softspace

file.write("Python 是一个很好的语言，这你承认吧？")
file = open("test.txt", "r+")
ss = file.read(10)
print '读取的结果为', ss
# 查找当前位置
position = file.tell()
print "当前文件位置：", position
ss = file.read(2)
print '继续上次的位置', ss
# 把指针再次重新定位到文件开头
position = file.seek(0, 0)
str = file.read(8)
print "重新读取字符串：", str
# 重命名文件
os.rename("test.txt", "first.txt")

# close()方法
file.close()

# 异常处理
try:
    first = open("test.txt", "w")
    first.write("嗯嗯，你说啥都对，谁让你那么帅呢？")
    b = 1 / 0
except IOError:
    print 'Error:没有找到文件或读取文件失败'
except ZeroDivisionError:
    print 'ZeroDivisionError:0不能作为除数！！！'
else:
    print '文件写入成功'
    first.close

# try-finally 语句
try:
    a = 0
    b = 'A'
    print b / a
except:
    print "I'm wrong,baby"
finally:
    print 'whatever 最后我还是执行了'


def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print '传入的参数中没有包含数字！！\n', Argument


temp_convert('abc')
timep_ = temp_convert('123')
print '解析数据为：', timep_


# 触发异常
def my_level(level):
    if level < 5:
        raise Exception("Invalid level", level)
        # 触发异常后，后面的代码就不会再执行


# try:
# 	my_level(1)
# except 'Invalid level':
# 	print '无效的参数。。。。。'
# else:
# 	print 'you made it'

# 用户自定义异常
class Networkerror(RuntimeError):
    """继承自运行时错误的自定义异常"""

    def __init__(self, arg):
        self.arg = arg


try:
    raise Networkerror("Bad hostname")
except Networkerror, e:
    print e.arg


