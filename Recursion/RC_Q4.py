def power(num,p):
    if p<1:
        return 1
    else:
        return num*power(num,p-1)
    
print(power(5,3))    