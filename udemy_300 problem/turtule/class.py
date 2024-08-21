class User:
    name=''
    email=''
    password=''
    login=False

    def login(self):
        email =input("enter email=")
        password=input("Enter password=")

        if email == self.email and password ==self.password:
            login = True
            print ("login successful")

        else:
            print ("login faild")

            def logout(self):
                login =False
                print("logout")

                def islogin(self):
                    if self.login:
                        return True
                    else:
                        return False
                    
                    def profile (self):
                        if self.islogin():
                            print(self.name,"\n",self.email)
                        else:
                            print("user is not login")

user1 = User()  
user1.name="sohag"
user1.email="mdsohaghossain138643@gmail.com"
user1.password="138643"

user1.login()
                        
