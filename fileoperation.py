poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''

#指定是以write方式打开相应文件
file = open("poem.txt","w")
file.write(poem)
file.close()

#默认是read方式
file = open("poem.txt")
while True:
    line = file.readline()
    if len(line) == 0:
        break
    print(line,end="")
file.close()


