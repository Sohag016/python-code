total_class= int (input('Enter Total class='))
total_attendance= int (input('Enter Total attendance ='))

result= (total_attendance/total_class)*100
print('Student attendance=',result)

if(result>=75):
    print('Student is collegiate')
else:
    print('Student is Non collegiate')