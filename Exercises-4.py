# count = 1
# while count != 11:
#     print(count)
#     count+= 1

# count = 10
# while count != 0:
#     print(count)
#     count-= 1
# print("start")

# count = 1
# while count != 51:
#     if count % 2 == 0:
#      print(count)
#     count+= 1
 
# num = int(input("enter a num"))
# count = 0
# count1 = num
# while count != num:
#     print(count1)
#     count1 += num
#     count += 1

# count = 1
# count1 = 0
# while count != 101:
#     count1 += count
#     count += 1
# print(count1)

# a = "Python123"
# b = input("pasword")
# while b!= a:
#     b = input("pasword")
# print("Welcome!")

# secret_number = 27
# num = int(input("enter a num"))
# while num != secret_number:
#     num = int(input("enter a num"))
# print("hhhhhhhhhhiiiiiiiiiiii")


# count = 0
# num = int(input("enter a num"))
# while num != 0:
#     count += num
#     num = int(input("enter a num"))
# print(count)

# count = 0
# sum_grade = 0
# while True:
#     num = int(input("enter a num"))
#     if num == 999:
#         break 
#     else:
#         count+=1
#         sum_grade += num
# print(count)
# print(sum_grade)
# print(sum_grade/count)


# count = 0
# sum_num = 0
# while True:
#     num = int(input("enter a num"))
#     if num < 0:
#         break 
#     else:
#         count+=1
#         sum_num += num
# print(count)
# print(sum_num)

# count = 1
# num = int(input("enter a num"))
# while count != 11:
#     print(num,"x",count,"=",num*count)
#     count+=1

# count = 0
# num = int(input("enter a num"))
# while num != 0:
#     num //= 10
#     count+= 1
# print(count)


# number = ""
# num = int(input("enter a num"))
# while num != 0:
#     number += str(num % 10)
#     num //= 10
# print(int(number))

# num = int(input("enter a num"))
# count = 2
# flag = True
# while count != num:
#     if num % count == 0:
#         flag = False
#         break
#     count += 1
# print(flag)

# balance = 5000
# while True:
#     print("""1.Check balance.
# 2.Deposit money.
# 3.Withdraw money.
# 4.Log out.""")  
#     choice = input("Enter your choice")
#     if choice == "1":
#         print(balance)
#     elif choice == "2":
#         num = int(input("enter a sum"))
#         if num > 0:
#             balance+= num
#     elif choice == "3":
#         num = int(input("enter a sum"))
#         if num > 0 and num <= balance:
#             balance-= num
#     elif choice == "4":
#         break

# count = 0
# while True:
#     count += 1
#     print(count)
#     if count == 15:
#         break

# count = 0
# while count != 31:
#     if count % 3 == 0:
#         count +=1
#         continue
#     else:
#      print(count)
#      count += 1

# while True:
#     num = int(input("enter a num"))
#     if num == 100:
#         print("hhhhhiiii")
#         break

# for num in range(1,21):
#     print(num)


# for num in range(101):
#     if num % 5 == 0:
#         print(num)


# count = 0
# for num in range(101):
#     count += num
# print(count)

# num1 = int(input("enter a num"))
# for num in range(1,11):
#     print(num,"x",num1,"=",num*num1)


# num1 = int(input("enter a num"))
# num2 = int(input("enter a num"))
# count = 0
# for num in range(num1,num2+1):
#     count += num
# print(count)

# for num in range(101):
#     if num %3 ==0 and num% 5 == 0:
#         print(num)

# num1 = int(input("enter a num"))
# num2 = int(input("enter a num"))
# for i in range(num1):
#     print()
#     for j in range(num2):
#         print("*",end=" ")
        
# for i in range(10):
#     print()
#     for j in range(i):
#         print("*",end= "")

# for i in range(1,11):
#     print()
#     for j in range(1,11):
#         print(i*j,end= "\t")

# for i in range(1,6):
#      for j in range(1,6):
#          print(i,",",j)
#          print()



# count = 0
# while True:
#     print("""
# 1. Start Game
# 2. View Instructions
# 3. Exit
# """)
#     Choose = input("Choose:")
#     if Choose == "1":
#         for i in range(1,11):
#             print(1,"x",i,"=")
#             Choose1 = int(input("Choose:"))
#             if Choose1 == 1*i:
#                 count+=1
#         print(count) 
#         count = 0       
#     elif Choose == "2":
#         print("Each correct answer earns one point.")
#     elif Choose == "3":
#         break
#     else:
#         print("1-3 only")   