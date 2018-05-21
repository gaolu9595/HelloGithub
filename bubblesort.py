inputnum = input("enter a number list here:")
numberlist = inputnum.split(" ")
print(numberlist)

nums = [1,33,24,45,89,22,37,28,57,278,100]
#从小到大排序
#冒泡排序
def bubbleSort(list):
    for i in range(len(list)-1) :
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list

#注意要把类型转换成int哦！！！！！！
print("input result:",bubbleSort(numberlist))
print("setted result:",bubbleSort(nums))










