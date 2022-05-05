
while True:
 list1=[0,0,0,0,0,0,0,0]   
 g=input('number')
 y=int(g)
 for i in range (7,0,-1):
    if y//(2**i)>=1:
        x=7-i
        list1[x]=1
        t=y%(2**i)
        if t>1:
          y=t
          i=0
          continue
        elif t==1:
            list1[7]=1
            break
        else:
            break
   
 print(list1)
     
