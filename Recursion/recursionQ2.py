def oper(num):
    if num<1:
        return 1
    oper(num-1)
    print(num,end=' ')
    oper(num-1)
    return

oper(3)


