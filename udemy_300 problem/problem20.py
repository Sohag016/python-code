#get 5 number from the user
#store in the array and display
#find their  python code
# Initialize an empty list to store the numbers
number=[]

for i in range(5):
    num=int(input('Enter number {i+1}:'))
    
    number.append(num)
# Display the numbers
print('The numbers you entered are:',number)
# Calculate the sum of the numbers
total_sum = sum(number)

# Display the total sum
print("The sum of the numbers is:", total_sum)