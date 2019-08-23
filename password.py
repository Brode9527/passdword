password = 'a123456'
i = 3
while i > 0:
    i = i - 1 
    key = input('請輸入密碼：')
    if key == password:
        print('登入成功')
        break
    else:
        print('密碼錯誤')
        if i > 0:
            print('你還剩', i,'次機會')
        else:
            print('沒機會嘗試了！要鎖帳號了啦！')