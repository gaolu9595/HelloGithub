#lambda函数语法
points = [{'x': 2, 'y': 3},
{'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)

#列表推导
listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)

#assert断言，断言失败时抛出AssertionError
mylist = ["item"]
assert len(mylist)<1
mylist.pop()
