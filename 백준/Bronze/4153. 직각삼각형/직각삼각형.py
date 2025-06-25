while True:
    x, y, z = map(int, input().split())
    l = sorted([x,y,z])
    if x == 0 and y == 0 and z == 0:
        break

    if l[0]**2  + l[1]**2 == l[2]**2:
        print('right')
    else:
        print('wrong')