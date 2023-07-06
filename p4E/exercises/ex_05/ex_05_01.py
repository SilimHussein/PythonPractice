cnt = 0
tot = 0.0
while True:
    num = input('please enter a number :')
    if num == 'done':
        break
    try:
        fnum = float(num)
    except:
        print('invalid input ')
        continue
    #print(fnum)
    cnt = cnt + 1
    tot = tot + fnum
print('total =', tot, 'count = ', cnt, 'average = ', tot/cnt)
    

