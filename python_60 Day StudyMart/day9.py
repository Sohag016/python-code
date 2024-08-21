subjects=['ai','data science','statistics','math']
for x in subjects:
    print(x)

def factorial(n):
    if(n == 0):
        return 1
    else:
        return n * factorial(n-1)
n=7
result=factorial(n)
print(f'factorial number {n} is {result}')
#fact=1   
#n=int (input('Enter any number='))
#for i in range(1,n+1):
    
    #fact=fact*i 

#print('factorial=',fact)      
for number in range(-100,-9):
    print (number)


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_primes_in_range(start, end):
    prime_sum = 0
    for number in range(start, end + 1):
        if is_prime(number):
            prime_sum += number
    return prime_sum

# Define the range
start = 10
end = 1000

# Calculate the sum of prime numbers within the range
prime_sum = sum_primes_in_range(start, end)

print(f"The sum of all prime numbers between {start} and {end} is {prime_sum}")

data= 'i love data Science so much'
data= data.split()
for i in range(len(data)):
    print(data[i])


n= int(input('Enter any number='))
a=[ ]
sum=0
for i in range (n):
    element=int(input(f'Enter number{i+1} = '))
    a.append(element)
    sum=sum+element
    print ("ARRAy=",a)
print('summation=',sum)


for i in range(1,100,2):#start,end , increament
    print ('Sohag',i)