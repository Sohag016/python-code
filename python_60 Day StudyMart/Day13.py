list1=[1,2,3,{'so',1,3},'sohag']
print(list1)
#copy()
list2=list1
list3=list1.copy()
list1[0]='1000'
print(list1)
print(list2)
print(list3)
list3[0]=1000
print(list3)
#append ()
list1.append(20)
print(list1)
#insert()
list1.insert(0,'sohag')
print(list1)
#index ()
list1.count(1)
print(list1)

a=[]
for i in range(1,5):
    new=int(input())
    a.append(new)
    
    print(a)
    element=sum(a)
    print (element)

