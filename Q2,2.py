list1=[]
while True:
 g=input('number')
 y=int(g)

 for i in range (0,7):
    x=y//2
    t=y%2
    list1.append(t)
    y=x    
 list1.reverse()
 print(list1)
     
