# numbers = (10,20,30,40,50)
# print(numbers)
# print(numbers[0],numbers[-1])
# print(len(numbers))
# print(numbers[2])

# names = ("avi","nati","dani","yossi","hiim")
# for name in names:
#     print(name)
# if "nati" in names:
#     print("yes")
# else:
#     print("no")


# numbers = (1,2,3,4,5,6,7)
# print(numbers[:3])
# print(numbers[-3:])
# print(numbers[::-1])

# product = ("aaa",100,10,"bbb")
# print(product[0])
# print(product[1])
# print(product[2])
# print(product[3])

# numbers = (1,2,3,4,5,6,7)
# sum1 = 0
# count = 0
# big = numbers[0]
# for num in numbers:
#     sum1 += num
#     if num > big:
#         big = num
#     if num % 2 == 0:
#         count+=1
# print(big)
# print(count)
# print(sum1)

# products = ("Laptop", "Mouse", "Keyboard", "Screen", "Printer")
# first = products[:3]
# last = products[-2:]
# all = first + last
# print(all)

# student = {"name":"David","age": 22,"grade": 95,"city":"Tel Aviv"}
# print(student["name"])
# print(student["age"])
# print(student["grade"])
# print(student["city"])

# car = {"brand": "toyota","model":"sadan","year":2020,"price":80000}
# car["color"] = "blue"
# car["year"]= 2023
# car["price"] = 90000
# print(car)

# salaries = {"David": 12000,"Moshe": 15000,"Dana": 13500}
# for i in salaries:
#     print(salaries[i])
# salaries["Dana"] = 15500
# salaries["nati"] = 22000
# print(salaries)

# products = {"Laptop":3500, "Mouse":100,"Keyboard":250,"Screen":400,"Printer":500}
# product = input("product: ")
# for p in products:
#     if product == p:
#         print(products[p])
#         break
# else:
#     print("not found")

# grades = {"David": 90,"Moshe": 75,"Dana": 100,"Noa": 55,"Avi": 82}
# for grade in grades:
#     print(grade," \t| ",grades[grade])
# for grade in grades:
#     if grades[grade] >= 80:
#         print(grade)
# count = 0
# for grade in grades:
#     count+=grades[grade]
# print(count/len(grades))
# name =None
# big = 0
# for grade in grades:
#     if grades[grade] > big:
#         name = grade
#         big = grades[grade]
# print(name,big)
# failds = 0
# for grade in grades:
#     if grades[grade] < 60:
#         failds += 1
# print(failds)


# products = {"Laptop":3500, "Mouse":100,"Keyboard":250,"Screen":400,"Printer":500}
# product = input("product: ")
# for p in products:
#     if product == p:
#         price = int(input("price: "))
#         products[p] = price
#         break
# else:
#     print("not found")
#     product = input("product: ")
#     price = int(input("price: "))
#     products[product] = price
# print(products)


# students = [{"name": "David", "age": 20, "grade": 90},{"name": "Moshe", "age": 22, "grade": 75},{"name": "Dana", "age": 21, "grade": 100},{"name": "Noa", "age": 19, "grade": 55},{"name": "Avi", "age": 23, "grade": 82}]
# for student in students:
#     print(student["name"])

# for student in students:
#     print(student["grade"])
    
# for student in students:
#     if student["grade"] >= 80:
#         print(student["name"])

# count = 0
# for student in students:
#     count += (student["grade"])
# print(count/len(students))

# big = 0
# for student in students:
#     if student["grade"] > big:
#         big = student["grade"]
# for student in students:
#     if student["grade"] == big:
#         print(student)
#         break

# students = [{"name": "David", "age": 20, "grade": 90},{"name": "Moshe", "age": 22, "grade": 75},{"name": "Dana", "age": 21, "grade": 100},{"name": "Noa", "age": 19, "grade": 55},{"name": "Avi", "age": 23, "grade": 82}]
# students.append({"name":"nati","age":22,"grade":99})
# for student in students:
#  if student["name"] == "nati":
#     student["grade"] = 100
# for student in students:
#     if student["name"] == "David":
#         students.remove(student)
# print(students) 
# 

# classroom = {"Class A":["David", "Moshe", "Dana"],"Class B":["Noa", "Avi", "Michael"],"Class C":["Daniel", "Shir", "Yossi"]} 
# for clas in classroom:
#     print(clas)
# print(classroom["Class A"])
# classroom["Class B"].append("Nati")
# classroom["Class C"].remove("Shir")
# print(len(classroom["Class A"]))
# print(len(classroom["Class B"]))
# print(len(classroom["Class C"]))

# products = {"Laptop": {"price": 4500,"stock": 10},"Mouse":{ "price": 80,"stock": 50},"Keyboard": { "price": 150,"stock": 20 }}
# for product in products:
#     print(product,products[product]["price"])
# for product in products:
#     print(product,products[product]["stock"])
# products["Laptop"]["stock"] = 25
# products["aaa"] = {"price": 450,"stock": 15}
# for product in products:
#     if products[product]["price"] > 100:
#         print(product)

# employees = [("David", "Development", 15000),("Moshe", "Marketing", 12000),("Dana", "Development", 18000),("Noa", "HR", 11000)]
# for employe in employees:
#     print(employe[0])
# for employe in employees:
#     if employe[1] == "Development":
#         print(employe)
# must = 0
# for employe in employees:
#     if employe[2] > must:
#         must = employe[2] 
# for employe in employees:
#     if employe[2] == must:
#         print(employe)
# count = 0
# for employe in employees:
#     count += employe[2]
# print(count/len(employees))

# inventory = {"Laptop": 10,"Mouse": 50,"Keyboard": 20}
# name = input("name")
# amount = int(input("amount"))
# for product in inventory:
#     if name == product:
#         if amount <= inventory[product]:
#             inventory[product] -= amount
#             break

#         else:
#             print("Not enough stock")
#             break
# else:
#     print("not found")
# print(inventory)   

# votes = {"David": 0,"Moshe": 0,"Dana": 0}
# while True:
#     name = input("name")
#     if name == "stop":
#         break
#     elif name in votes:
#         votes[name] += 1
#     else:
#         print("There is no such candidate.")
# print(votes)
# count = 0
# for name in votes:
#     if votes[name] > count:
#         count = votes[name]
# for name in votes:
#     if votes[name] == count:
#         print(name,votes[name])



# Contacts= {"avi":"0550000000","dani":"05600000000","yossi":"0540000000"}
# while True:
#     print("""
# 1. Add a contact.
# 2. Search for a contact.
# 3. Update a phone number.
# 4. Delete a contact.
# 5. View all contacts.
# 0. Exit.
# """)
#     choice = input("choice: ")
#     if choice == "1":
#         name = input("name: ")
#         number = input("number: ")
#         Contacts[name] = number
#     elif choice == "2":
#         name = input("name: ")
#         for n in Contacts:
#             if n == name:
#                 print(n,Contacts[name])
#     elif choice == "3":
#         name = input("name: ")
#         for n in Contacts:
#             if n == name:
#                 number = input("number: ")
#                 Contacts[name] = number
#                 break
#         else:
#             print("not found")
#     elif choice == "4":
#         name = input("name: ")
#         for n in Contacts:
#             if n == name:
#                 Contacts.pop(name)
#                 break
#         else:
#             print("not found")          
#     elif choice == "5":
#         for name in Contacts:
#             print(name,"\t",Contacts[name])
#     elif choice == "0":
#         break
#     else:
#         print("0-5")

# products = [{"name": "Laptop", "price": 4500, "stock": 10},{"name": "Mouse", "price": 80, "stock": 50},{"name": "Keyboard", "price": 150, "stock": 20},{"name": "Screen", "price": 900, "stock": 15}]
# while True:
#     print("""
# ===== Store Management =====

# 1. Show all products
# 2. Add product
# 3. Search product
# 4. Update product price
# 5. Update product stock
# 6. Sell product
# 7. Show products by price
# 8. Show products with low stock
# 9. Show total inventory value
# 0. Exit

# """)
#     choice = input("choice: ")
#     if choice == "1":
#         for product in products:
#               print(product)
#     elif choice == "2":
#         new_product = {}
#         name = input("name: ")
#         new_product["name"] = name
#         price = int(input("price: "))
#         new_product["price"] = price
#         stock  = int(input("stock: "))
#         new_product["stock"] = stock
#         products.append(new_product)
#     elif choice == "3":
#         name = input("name: ")
#         for p in products:
#             if p["name"] == name:
#                 print(p)    
#     elif choice == "4":
#         name = input("name: ")
#         for p in products:
#             if p["name"] == name:
#                 price = int(input("price: "))
#                 p["price"] = price              
#     elif choice == "5":
#         name = input("name: ")
#         for p in products:
#             if p["name"] == name:
#                 stock  = int(input("stock: "))
#                 p["stock"] = stock 
#     elif choice == "6":
#        name = input("name: ")
#        amount = int(input("amount: "))
#        for p in products:
#         if p["name"] == name:
#             if p["stock"] >= amount:
#                 p["stock"] -= amount
#             else:
#                 print("Out of stock")
#     elif choice == "7":
#         price = int(input("price: "))
#         for p in products:
#             if p["price"] > price:
#                 print(p)      
#     elif choice == "8":
#         low_stock = [p for p in products if p["stock"] < 10]
#         print(low_stock)
#     elif choice == "9":
#         count = 0
#         for p in products:
#             count += (p["price"]*p["stock"])
#         print(count)
#     elif choice == "0":
#         exit()
#     else:
#         print("0-9 only")