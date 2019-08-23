password = 'a123456'
i = 3
while True:
    key = input('請輸入七位數密碼(最多三次)：')
    if key == password:
        print('登入成功')
        break
    else:
        i = i - 1 
        print('密碼錯誤，你還剩', i,'次機會')
        if i == 0:
            print('請改天再嘗試，再見！！！！')
            break