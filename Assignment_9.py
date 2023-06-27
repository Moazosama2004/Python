# Assignment 1

print("Choose One Of them => + Or - Or * Or / Or ")
num1 = int(input("Enter First Num : ").strip())
num2 = int(input("Enter Second Num : "))
operation = input("Enter Your Operation : ").strip()

if operation == "+" :
    print(num1 + num2)
elif operation == "-" :
    print(num1 - num2)
elif operation == "*" :
    print(num1 * num2)
elif operation == "/" :
    print(num1 / num2)
else :
    print("Enter a Valid Operation pls ..")

print("=" * 30)

# Assignment 2

age = 17

print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You")
print("=" * 30)

# Assignment 3

age = int(input("Enter Your Age : ").strip())

months = age * 12
weeks = months * 4
days = weeks * 7
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"Your Age In Months Is {months} Months")
print(f"Your Age In Weeks Is {weeks} Weeks")
print("=" * 30)

# Assignment 3

# Input Example One "Egypt"
# Input Example Two "Ghana"

country = input("Input Your Country ").capitalize().strip()
countries = ["Egypt", "Palestine", "Syria","Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country in countries:
    print(
        f"Your Country Eligible For Discount And The Price After Discount Is {price - discount}")
else:
    print(f"Your Country Not Eligible For Discount And The Price Is {price}")

