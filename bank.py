print("WELCOME TO FATICHAR BANK")
unm=input("Enter Your Full Name Please :")
print("Welcome Mr. " + unm + "to FATICHAR BANK")
print("")
print("Choose what do you wanna")
#for sign up form
sgn=input("SIGNUP/LOGIN"  )
if (sgn=='signup'):
                print("Create Your new A/C No:")
                print(" ")
                fnm=input("Entter Your First Name : ")
                gndr=input("Enter Your SEX :")
                lnm=input("Enter Your Last Name : ")
                cont=int(input("Enter Your Contact No : "))
                cntry=input("Your Cpuntry Name :")
                add=input("Enter Your Permanent Address: ")
                pradd=input("Enter Your Present Address : ")
                exit()
                


#for exixting account numer
else:
     print("Mr. "+ unm + "Enter You Mail ID to enter your Existing Account")
     for i in range (3):
                        mail=input("Enter Your Mail ID : ")
                        j=2
                        if (mail=="john@gmail.com"):
                            print("Enter Your Password of your account")



'''
 print("NOW YOU HAVE TO ENTER YOUR A/C NO")
for i in range(3):
                uac=int(input("Enter Here Your 9 Digit A/C no : "))
                j=2
                if(uac==123456789):
                        print("It's Good Mr. " + unm + "You've enter correct A/C No.")
                        print("")
                        amt=10000
    
                        
                else:
                        print("Wrong A/C No. You can enter", j-i,"more times")
                        continue
print("Oops! enter again your passowrd")
'''

    
    
        
