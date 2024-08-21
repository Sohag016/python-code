attendance = int (input('Enter your attendance='))
total_Class =int (input('Enter your total class='))
result = (attendance/total_Class)*100
print('your attendance=',result)

if(result>=75):
    print('Your are collegiate Student')
else:
    print('Non Collegiate')