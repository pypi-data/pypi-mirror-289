def upperc(x):
    with open(x,'r') as f:
        c=f.read()
        f.close()
    ucon=c.upper()
    
    print("enter new file name for ",y,"MB")
    name=input(" ")	
    na=name+'.txt'
    with open(na,'w') as f1:
        f1.write(ucon)
        f1.close()
    print("contents are uppercase in file ",na)