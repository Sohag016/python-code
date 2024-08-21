# nasted loop
for i in range(1,3+1):
    for j in range(i):
        print('*',end=' ')
    print('')
    

num=[1,2,3,4]
#outer
for i in num:
    #inner
    j=0
    while j<len(num):
        print(num[j],end=' ')
        j+=1
    print(' ')        