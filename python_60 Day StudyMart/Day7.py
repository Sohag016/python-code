a = int (input('Enter three number='))
b = int (input('Enter three number='))
c = int (input('Enter three number='))
if(a>=b and a>=c):
    print(a)
elif(b>=a  and b>=c):
     print(b)  

else:
     print(c)


num = int (input('Enter any Number='))
if(num>100):
     print('Invalid')
elif(num>=80 and num<=100 ):
     print('A+')  
elif(num>=70 and num<80):
     print('A')
elif(num>=60 and num<70):
     print('B+')
elif(num>=50 and num<60):
     print('B')  
elif(num>=40 and num<50):
     print('C')
elif(num>=33 and num<40):
     print('D') 
else:
     print('F')