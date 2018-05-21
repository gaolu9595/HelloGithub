#coding = UTF-8

def trims(s):
    while s[0] == " ":
        s = s[1:len(s)]
    while s[-1] == " ":
        s = s[0:len(s)-1]
    return s

text = input("enter a string:")
print(text)
print(trims(text))

#列表生成式
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)
#生成器
L3 = (s.lower() for s in L1 if isinstance(s,str))
print(L3)
for item in L3:
    print(item)

#斐波拉契数列
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        a,b = b,a+b
        n = n+1
        print(a)

fib(6)
