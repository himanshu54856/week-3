l=[("sachin tendulkar",34357),("ricky ponting",27483),("jack kallis",25534),("virat kohli",24936)]
l.sort(key=lambda x:x[1])
print(l)


l=[1,2,3,4,5,6,7,8,9,10]
m=list(map(lambda x:x**2 ,l))
print(m)
    



l=[1,2,3,4,5,6,7,8,9,10]
print(tuple(l))
   



l=(2,3,6,9,27,60,90,120,55,46)
for i in range(l):
    if (i%2==0) or (i%3==0):
           print(i)   



t=["python","phy","radar","level"]
r=list(filter(lambda x:(x=="".join(reversed(x))),t)) 
print(r)           
