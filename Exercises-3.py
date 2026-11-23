# age = int(input("enter your age"))
# if age >= 18:
#     print("adult")
# else:
#     print("minor")
# 
# num = int(input("enter a num")) 
# if num > 0:
#     print("positive")
# elif num == 0:
#     print("zero")
# else:
#     print("negative")       
# 
# num = int(input("enter a num"))
# if num % 2 == 0:
#     print("Even")    
# else:
#     print("Odd")    
# num1 = int(input("enter a num"))
# num2 = int(input("enter a num"))
# if num1 > num2:
#     print(num1)
# elif num1 == num2:
#     print("The numbers are equal.")  
# else:
#     print(num2)  
# 
#     
# password = "Python123"
# password_1 = input("enter password" )
# if password_1 == password:
#     print("Access Granted")
# else: 
#     print("Access Denied")   

# num1 = int(input("enter a num"))
# if num1>0 and num1<= 10:
#     print("1-10")
# elif num1>10 and num1<= 50:
#     print("11-50")
# elif num1>50 and num1<= 100:
#     print("51-100")
# else:
#     print("Out of range")        


# num1 = int(input("enter a grade"))
# if num1>=90 and num1<= 100:
#     print("Excellent")
# elif num1>=80 and num1< 90:
#     print("Very Good")
# elif num1>=70 and num1<80:
#     print("Good")
# elif num1>=60 and num1<70:
#     print("Passed")
# elif num1>=0 and num1<60:
#     print("Failed")          
# else:
#     print("Invalid Grade")

# correct_username = "admin"
# correct_password = "123456"

# correct_username_1 = input("username:")
# correct_password_1 = input("password:")
# if correct_username_1 == correct_username and correct_password_1 == correct_password:
#     print("Login Successful")
# elif correct_username_1 == correct_username:
#     print("Wrong Password")
# else:
#     print("Unknown User")    


# age = int(input("enter your age"))
# price = int(input("enter your price"))
# if age > 60:
#     print(price * 0.8)
# elif age < 18:
#     print(price * 0.9)    
# else:
#     print(price)    

# num1 = int(input("enter a num"))
# if num1 % 3 == 0 and num1 % 5 ==0:
#     print("The number is divisible by five and three.")
# elif num1 % 3 == 0:
#     print("The number is divisible by three.")    
# elif num1 % 5 == 0:
#     print("The number is divisible by five.") 
# else:
#     print("The number is not divisible by five and three.")  
# 
# age = int(input("enter your age"))
# escort = input("Does he have a companion?")
# if age >= 18:
#     print("Authorized to enter")
# elif age >= 16:
#     if escort == "true":
#         print("Authorized to enter")    
# else:
#     print("Not permitted to enter")        

# num1 = int(input("enter avg grade:"))
# Monthly_Income = int(input("enter Monthly Income:"))
# if num1 > 90:
#     print("Eligible for a scholarship")
# elif num1 > 85 and Monthly_Income < 5000:
#     print("Eligible for a scholarship")
# else:
#    print("not Eligible for a scholarship")       
# 
# correct_username = "admin"
# correct_password = "123456"
# correct_username_1 = input("username:")
# correct_password_1 = input("password:")
# activ = input("activ:")
# if correct_username_1 == correct_username and correct_password_1 == correct_password and activ == "true":
#     print("Entry approved")
# else:
#     print("Entry was not approved.")

# num = int(input("enter a num")) 
# if num >= 20 and num <= 80:
#     print("yessss")
# elif not num >= 20 and num <= 80:
#     print("noooooo")  
# 
# balance = 5000
# num = int(input("Enter amount for withdrawal: "))
# if num > 0:
#     if num <= balance:
#         balance-= num
#         print(balance)
#     else:
#         print("The amount is greater than the balance.")
# else:
#     print("The amount must be positive.")

# age = int(input("enter your age"))
# activ = input("activ:")
# if age <= 12 :
#     if activ == "true":
#         print(25 * 0.9)
#     else:
#         print(25)    
# elif age <= 18:
#     if activ == "true":
#         print(35 * 0.9)
#     else:
#         print(35)
# elif age > 18:
#     if activ == "true":
#         print(50 * 0.9)
#     else:
#         print(50)

# age = int(input("enter your age"))
# Monthly_Income = int(input("enter Monthly Income:"))
# seniority = int(input("enter your seniority"))
# if age >= 21:
#     if Monthly_Income >= 7000:
#         if seniority >=1:
#             print("Eligible for a loan")
#         else:    
#          print("At least one year of experience is required")
#     else:     
#        print("You need a salary of at least 7,000 NIS.")
# else:
#    print("Must be 21 years of age or older")

# print("""
# 1 Motorcycle
# 2 Private vehicle
# 3 Commercial vehicle
# """)
# choice = input("Enter your choice")
# time = float(input("How long were you in the parking lot?"))
# if choice == "1":
#     if time <= 1:
#         print(10 *time * 0.9) 
#     elif time> 5:
#         print(10 *time * 0.85) 
#     else:
#         print(10 *time)
# elif choice == "2":
#     if time <= 1:
#         print(20 *time * 0.9) 
#     elif time> 5:
#         print(20 *time * 0.85) 
#     else:
#         print(20 *time)
# elif choice == "3":
#     if time <= 1:
#         print(30 *time * 0.9) 
#     elif time> 5:
#         print(30 *time * 0.85) 
#     else:
#         print(30 *time)

# num1 = int(input("enter a num"))
# num2 = int(input("enter a num"))
# Operator = input("Enter the desired accounting operation")
# if Operator == "+":
#     print(num1 + num2)
# elif Operator == "-":
#     print(num1 - num2)
# elif Operator == "*":
#     print(num1 * num2)
# elif Operator == "/":
#     if num2 == 0:
#       print("It is impossible to divide by zero.")
#     else:  
#       print(num1 / num2)
# else:
#    print("Illegal action")

# year = int(input("enter a year"))
# if year % 400 == 0:
#     print("leap year")
# elif year % 100 == 0 and year % 400 != 0:
#     print("not leap year")
# elif year % 4 == 0 and year % 100 != 0:
#     print("leap year")    
# else:
#     print("not leap year")

# Hourly_wage = float(input("Enter the number of monthly hours"))
# if Hourly_wage <= 182:
#     print(Hourly_wage * 50)
# elif Hourly_wage <= 184:
#     print(182* 50 + ((Hourly_wage - 182) *(50*1.25)))
# else:
#     print((182* 50 + (2 *(50*1.25)))+ ((Hourly_wage -184) * (50*1.5)))

# client_age = input("Enter your age ")
# order_price = int(input("Enter order price "))
# is_membership= input("are you membership (True/False)")
# is_product_open = input("are the product open (Yes/No)")
# is_have_recipt = input("do you have the recipt Yes/No)")
# order_time = int(input("Enter how meny dayes is after the order"))
# if is_have_recipt == "Yes":
#     if is_product_open == "No":
#         if order_price > 0:
#             if is_membership == "Yes":
#                 if order_time <=30 :
#                   print("Eligible for a refund",order_price)
#                 else:
#                     print("Not eligible; more than thirty days have passed.")
#             else:
#                 if order_time <=14 :
#                     print("Eligible for a refund",order_price)
#                 else:
#                     print("Not eligible; more than 14 days have passed.")
#         else:
#             print("The amount must be positive.")
#     else:
#         print("Not eligible; the product has been opened.")            
# else:
#     print("Not eligible; no receipt.")            

