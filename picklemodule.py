#持久化存储对象的模块：Pickle
#可以将任何纯Python对象存储到一个文件中，并在稍后将其取回

import pickle

shoplistfile = "shoplistfile.data"

shoplist = ["apple","mango","banana"]

file = open(shoplistfile,"wb")
#pickle将shoplist对象转存至file中
pickle.dump(shoplist,file)
file.close()

del shoplist

file = open(shoplistfile,"rb")
#pickle实现从文件中载入对象
storedlist = pickle.load(file)
print(storedlist)

try:
    text = input('Enter something --> ')
    #使用with语句使得打开关闭文件的过程以十分干净的姿态完成
    with open("poem.txt") as f:
        for line in f:
            print(line,end="")
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))

