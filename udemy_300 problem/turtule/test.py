
'''list1=('physics','chemistry','maths')
print(list1)
print("Length=",len(list1))'''
list2=list(range(10))
print(list2)
print("Length=",len(list2))

list1,list2=['c++','java','python'],[100,200,300]
print(list1,list2)
print(max(list1))
print(max(list2))

str='hellow'
list1=list(str)
print(list1)
print(len(list1))

a=(123,'cc++','java','python')
list1=list(a)
print (list1)
print(len(list1))

list=['abcd',786,2.23,'sohag',70.2]
tinylist =[123,'jony']
print(list,tinylist)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist*2)
print(list + tinylist)

list1=['physics','chemistry',1997,2000]
list2=[1,2,3,4,5,6,7]
print("list1[0]=",list1[0])
print("list2[1:5]=",list2[1:5])

#Update
print("value available=",list1[2])
list1[2]=2001
print("update value=",list1[2])

#Delete
print(list1)
del list1[2]
print("deleteing index2=",list1)
del list2
print(list2)