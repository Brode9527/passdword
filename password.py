password = 'a123456'
i = 3
while i > 0:
    key = input('請輸入七位數密碼(最多三次)：')
    if key == password:
        print('登入成功')
        break
    else:
        i = i - 1 
        print('密碼錯誤，你還剩', i,'次機會')
       