def fibanocci(n):
    if n<=1:
        return n
    else:
        return fibanocci(n-1) + fibanocci(n-2)
print(fibanocci(6))


