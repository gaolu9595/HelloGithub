#encoding = UTF-8
class ShortInputException(Exception):
    '''一个由用户定义的异常类，继承于Exception类'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input("enter a text here:")
    file = open("poem.txt")
    print(file.read())
    if (len(text)) < 5:
        #raise 语句用于引发一次异常，即提供异常名以及抛出该异常类的对象
        raise ShortInputException(len(text),5)
except EOFError:
    print("Why did you do an EOF on me?")
except ShortInputException as ex:
    print("ShortInputException Error: The input was {0} long, expected at least {1}".format(ex.length,ex.atleast))
else:
    print("No Exception was raised!")
finally:
    file.close()
    print("(Cleaning Up...)File Closed!")
