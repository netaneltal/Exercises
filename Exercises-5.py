# numbers = [10,20,30,40,50]
# print(numbers[0])
# print(numbers[-1])
# print(numbers[2])


# stutents = ["avi","nati","dani",]
# print(len(stutents))
# print(stutents[0],stutents[-1])
# stutents[1] = "yosi"
# print(stutents)

# grade = [90,80,70,65,95]
# grade.append(98)
# grade.insert(0,100)
# grade[2] = 85
# print(grade)

# numbers = [10,20,30,40,50,60,70,80,90,100]
# numbers.pop(0)
# print(numbers)
# numbers.pop(-1)
# print(numbers)
# numbers.pop(3)
# print(numbers)

# product = ["aaa","bbb","ccc"]
# if "aaa" in product:
#     print("yes")
# if "ddd" not in product:
#     print("no")

# numbers = [10,20,30,40,50,60,70,80,90,100]
# for num in numbers:
#     print(num)

# numbers = [10,20,31,40,55,60,70,80,90,100]
# for num in numbers:
#      if num % 2 == 0:
#         print(num)

# grade = [90,80,70,65,95]
# count = 0
# for grade in grade:
#     count+=grade
# print(count)

# numbers = [10,20,31,40,55,60,70,80,90,100]
# big = numbers[0]
# for num in numbers:
#     if num > big:
#         big = num
# print(big)

# flag = False
# stutents = ["avi","nati","dani",]
# name = input("name:")
# for n in stutents:
#     if name == n:
#         flag = True
# if flag == True:
#     print("found")
# else:
#     print("not found")


# numbers = [10,20,31,40,55,60,31,80,90,100]
# num = int(input("num:"))
# for i in range(len(numbers)):
#     if numbers[i] == num:
#         print(i) 

# numbers = [10,20,31,40,55,60,31,80,90,100]
# count = 0
# for num in numbers:
#     if num > 50:
#         count +=1
# print(count)

# numbers = [10,20,31,40,55,60,31,80,90,100]
# numbers_2 = []
# for num in numbers:
#     if num % 2 ==0:
#         numbers_2.append(num)
# print(numbers_2)

# stutents = ["avi","nati","dani"]
# count = 0
# while count != len(stutents) :
#     print(count,stutents[count])
#     count+=1

# numbers = [10,20,31,40,55,60,31,80,90,100]
# print(numbers[:3])
# print(numbers[-3:])
# print(numbers[2:7])
# print(numbers[::-1])

# names = ["aa","bb","cc","dd","ee","ff","gg","hh","ii","jj"]
# print(names[::2])
# print(names[1:len(names):2])
# print(names[::-2])

# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# nums_1 = []
# nums_2 = [] 
# nums_3 = []
# nums_1.append(numbers[0:10]) 
# nums_2.append(numbers[10:21])
# nums_3.append(numbers[5:15])
# print(nums_1)
# print(nums_2)
# print(nums_3)

# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# nums_1 = []
# nums_2 = []
# a = len(numbers)//2
# nums_1.append(numbers[0:a])
# nums_2.append(numbers[a::])
# print(nums_1)
# print(nums_2)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_numbers1 = [num * 2 for num in numbers]
# new_numbers2 = [num * num for num in numbers]
# new_numbers3 = [num for num in numbers if num % 2 == 0]
# new_numbers4 = [num for num in numbers if num > 5]
# print(new_numbers1)
# print(new_numbers2)
# print(new_numbers3)
# print(new_numbers4)

# grades = [55, 90, 67, 100, 45, 82, 73, 30]
# grades1= [grade for grade in grades if grade >= 60]
# grades2= [grade for grade in grades if grade < 60]
# grades3= [grade +5 for grade in grades]
# print(grades1)
# print(grades2)
# print(grades3)

# names = ["Moshe", "David", "Dana", "Noa", "Michael", "Avi"]
# new_names1 = [name for name in names if len(name) > 4]
# new_names2 = [name.upper() for name in names]
# new_names3 = [name for name in names if name[0] == "D"]
# print(new_names1)
# print(new_names2)
# print(new_names3)

# numbers = [12, 7, 25, 30, 9, 44, 18, 3]
# new_numbers = [num for num in numbers if num % 3 == 0 and num > 10]
# print(new_numbers)


# numbers = []
# for num in range(10):
#     num = int(input("enter a num:"))
#     numbers.append(num)
# print(numbers)
# small = numbers[0]
# for num in numbers:
#     if num < small:
#         small = num
# print(small)
# big = numbers[0]
# for num in numbers:
#     if num > big:
#         big = num
# print(big)
# avg = 0
# for num in numbers:
#     avg += num
# print(avg/len(numbers))

# names = ["aaa","bbb","ccc","ddd","eee"]
# name = input("name")
# flag = False
# for n in names:
#     if n == name:
#         names.remove(name)
#         flag = True
#         break
# if flag == False:
#     print("not found")
# print(names)

# numbers = [1,45,80,46,55,78,99,40,80,50,4,10]
# new_number1 = [num for num in numbers if num%2 ==0 ]
# new_number2 = [num for num in numbers if num%2 !=0 ]
# new_number3 = [num for num in numbers if num > 20]
# print(new_number1)
# print(new_number2)
# print(new_number3)

# numers1 = [1,2,3,4,5,6,7,8,9,10]
# numbers2 = [11,12,13,14,15,16,17,18,19,20]
# new_numbers = numers1+numbers2
# print(new_numbers)
# print(new_numbers[:5])
# print(new_numbers[-5:])
# print(new_numbers[::-1])

# numbers = [1,45,80,46,55,78,50,99,40,80,50,4,10,50]
# num = int(input("number:"))
# count = 0
# flag = False
# for n in numbers:
#     if n == num:
#         numbers.remove(num)
#         count += 1
#         flag = True
# if flag == False:
#     print("not found")
# else:
#     print(count)




# numbers = [1,45,80,46,55,78,50,99,40,80,50,4,10,50]
# num = int(input("number:"))
# flag = False
# for n in numbers:
#     if n == num:
#         flag = True
#         break
# if flag == False:
#     numbers.append(num)
# print(numbers)

# grades = [85, 72, 90, 55, 100, 63, 48, 77]
# while True:
#     print("""
# ===== Grades Management =====

# 1. Show all grades
# 2. Add a grade
# 3. Search for a grade
# 4. Remove a grade
# 5. Show passing grades
# 6. Show failing grades
# 7. Show highest and lowest grade
# 8. Show average grade
# 9. Show first 3 grades
# 10. Show grades in reverse
# 0. Exit
# """)
#     choice = input("choice: ")
#     if choice == "1":
#         for grade in grades:
#             print(grade)
#     elif choice == "2":
#         grade = int(input("grade: "))
#         grades.append(grade)
#     elif choice == "3":
#         grade = int(input("grade: "))
#         for i in range(len(grades)):
#             if grades[i] == grade:
#                 print(i)
#     elif choice == "4":
#         grade = int(input("grade: "))
#         for i in range(len(grades)):
#             if grades[i] == grade:
#                 grades.pop(i)
#                 print("Successfully deleted")
#                 break
#     elif choice == "5":
#         new_grades1 = [grade for grade in grades if grade >= 60]
#         print(new_grades1)
#     elif choice == "6":
#         new_grades2 = [grade for grade in grades if grade < 60]
#         print(new_grades2)
#     elif choice == "7":
#         small = grades[0]
#         big = grades[0]
#         for grade in grades:
#             if grade <small:
#                 small = grade
#             if grade > big:
#                 big = grade
#         print(big)
#         print(small)
#     elif choice == "8":
#         count = 0
#         for grade in grades:
#             count += grade
#         print(count/len(grades))
#     elif choice == "9":
#         print(grades[:3])
#     elif choice == "10":
#         print(grades[::-1])
#     elif choice == "0":
#         exit()
#     else:
#         print("0-10 only")