str1='hellothere'

stack=list(str1)
rev=''
for i in range(len(stack)):
    rev+=stack.pop()

print(rev)
    
