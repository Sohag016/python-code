i=0
while(i<=10):
    print('sohag',i)
    i+=1


num = int(input('Enter any number='))
sum = 0
temp = num

while temp != 0:
    r = temp % 10
    sum = sum + r
    temp = temp // 10  

print('Sum of digits =', sum)