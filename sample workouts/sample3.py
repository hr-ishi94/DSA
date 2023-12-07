char = "hellohowareyou"

ls = list(char)
result=''

def replace(ls):
    if len(ls) <= 0:
        return ls
    else:
        if ls[0] == 'o':
            ls[0] = 's'
        return [ls[0]] + replace(ls[1:])

for i in replace(ls):
    result+=i

print(result)
