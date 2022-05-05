file = open("quize.txt","r")
list1=[]
d={}
x=0
name=input('your name is')
for line in file:
    detail = line.split(",")
    print(detail[0])
    select = input("your option is: ")
    if select == detail[1]:
          print("Correct")
          list1.append('correct')
          x+=1
    else:
          print("Incorrect")
          list1.append('Incorrect')
          x-=1
d[name]=list1
file2=open('the result.txt','a')

file2.writelines(d)
print(d)
print(x)

























        ##while True:


##    print("to stop this prosses enter 0")
##    y = int(input("enter munber"))
##
##    if y == 0:
##        break
##    list1 = []
##    for i in range(0, 5):
##        x = y//2
##        t = y % 2
##        list1.append(t)
##        y = x
##    list1.reverse()
##    print(list1)
