#to chack user password
password= input("Enter your password=")

if(password.isalnum()):
    print("your password is oke")
else:
    print("your password is not oke")