def string(data):
    unique=set()
    new=''
    for i in  data:
        if i not in unique:
            count=data.count(i)
            new+=str(count)+i
            data.replace(i,'')
            unique.add(i)
        
         
    data=new
    
    return data



result=string('EEEHHII')
print(result)