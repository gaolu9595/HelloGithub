def is_palindrome(text):
    #从输入文本的开始到结束进行序列切片，步长为-1表示返回翻转过的文本
    forbidden = ("!",",",".","?")
    cleantext = ""

    for i in range(0,len(text)):
        char = text[i:i+1]
        if char in forbidden:
            char = ""
        cleantext += char
    print(cleantext)
    reverse = cleantext[::-1]
    return cleantext == reverse

running = True
while running:
    something = input("Enter text: ")
    if is_palindrome(something):
        print("Yes,it's a palindrome")
        print("Done! You have got it!")
        break
    else:
        print("No,it's not a palindrome")
