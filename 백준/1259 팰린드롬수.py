while True:
    temp = input()
    if temp == '0':
        break
    while True:
        if len(temp)<1:
            print('yes')
            break
        if temp[0] != temp[-1]:
            print('no')
            break
        temp= temp[1:-1]

