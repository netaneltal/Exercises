# num1 = 25
# num2 = 7

# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)
# print(num1//num2)
# print(num1%num2)
# print(num1**num2)

# balance = 1000
# print(balance)
# balance += 250
# print(balance)
# balance -= 100
# print(balance)
# balance *= 2
# print(balance)
# balance /= 4
# print(balance)


# price = int(input("price:"))
# percentage_discunt = int(input("percentage discunt:"))
# print(price * (percentage_discunt/ 100))
# print(price -(price * (percentage_discunt/ 100)))

# price = int(input("price:"))
# Interest= int(input("Interest:"))
# print(price * (Interest/ 100))
# print(price+(price * (Interest/ 100)))

# grade_1 = float(input("enter your grade"))
# grade_2 = float(input("enter your grade"))
# grade_3 = float(input("enter your grade"))
# print((grade_1 + grade_2 + grade_3)//3 )

# first_name = "David"
# last_name = "Cohen"
# city = "Tel Aviv"

# print("Hello, my name is " + first_name+" " + last_name + " and I live in " + city+".")
# print(f"Hello, my name is {first_name} {last_name} and I live in {city}.")

# full_name = input("full name:")
# print(len(full_name))
# print(full_name.upper())
# print(full_name.lower())

# txt = input("enter txt")
# print(txt.upper())
# print(txt.lower())
# print(txt.capitalize())
# print(txt.title())

# txt = input("enter txt")
# print(txt)
# print(txt.strip())
# print(len(txt))
# print(len(txt.strip()))

# sentence = "I love Java programming"
# new_sentence = sentence.replace("Java","Python")
# print(new_sentence)
# count = sentence.count("love")
# print(count)
# is_start =sentence.startswith("I")
# print(is_start)
# is_end =sentence.endswith("programming")
# print(is_end)

# word = "Programming"
# print(word[0])
# print(word[-0])
# print(word[2])
# print(word[:3])
# print(word[-3:])
# print(word[::-1])


# a = "100"
# b = "25"
# c = 10
# d = 5.5
# print(int(a))
# print(float(b))
# print(str(c))
# print(int(d))
# print(type(int(a)))
# print(type(float(b)))
# print(type(str(c)))
# print(type(int(d)))

# age = input("Enter your age: ")

# print(int(age) + 10)

# Because it is not possible to perform a mathematical operation on a string.


# price = input("price befor tax")
# print(float(price) +float(price) * 0.18)


# first_name = input("name:")
# last_name = input("last_name:")
# age = int(input("age:"))
# salary = int(input("salary:"))
# seniority = input("seniority:")
# print(f"""
# Employee Card 
# First Name {first_name}
# Last Name {last_name}
# age   {age}
# Monthly Salary {salary} 
# Years of Seniority {seniority}
# Annual Salary {salary *12}
# Annual Salary Plus 5% {salary * 12 *1.05}
# Length of Full Name {len(first_name + last_name)}
# """)

# usd_rate = 3.25
# shekels = int(input("enter sum"))
# print(shekels *usd_rate)
# print(shekels * 3.75)
# print(shekels *usd_rate * 1.02)
# print(shekels * 3.75 * 1.02)


# first_name = input("name:")
# last_name = input("last_name:")
# birthdeayr = input("birthdeayr:")
# print(f"{first_name.lower()}.{last_name.lower()}.{birthdeayr}@gmail.com")


# txt = input("enter txt")
# print(txt)
# print(len(txt))
# print(txt.upper())
# print(txt.lower())
# print(txt[::-1])
# print(txt.count("a"))
# print(txt.replace(" ","-"))


Customer_name = input("enter your name:")
Product_name = input("enter product name:")
Unit_price = float(input("enter Unit price:"))
Quantity = int(input("Quantity:"))
Discount_percentage = float(input("enter Discount percentage:"))
VAT_percentage = int(input("enter VAT percentage."))

print(f"""
===============================
          PURCHASE INVOICE
================================

Customer: {Customer_name}
Product: {Product_name.upper()}

Unit Price: {Unit_price}
Quantity: {Quantity}

Subtotal: {Unit_price * Quantity}
Discount: {(Unit_price * Quantity)* Discount_percentage//100}
After Discount: {(Unit_price * Quantity)-((Unit_price * Quantity)* Discount_percentage//100)}

VAT: 18%
VAT Amount: {((Unit_price * Quantity)-((Unit_price * Quantity)* Discount_percentage//100))* 0.18}

TOTAL: {((Unit_price * Quantity)-((Unit_price * Quantity)* Discount_percentage//100))*1.18}

================================
       THANK YOU FOR SHOPPING
================================

""")