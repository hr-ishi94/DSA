def div(a,b):
    print(a/b)

def custom_div(func):
    def inner(a,b):
        if a<b :
            a,b = b,a 
        return func(a,b)
    return inner 


div = (custom_div(div))
div(2,4)