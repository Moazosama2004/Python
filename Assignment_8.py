# Assignment 1

name = input("What\'s Your Name ?").strip().capitalize()
print(f"Hello {name}, Happy To See You Here.")
print("=" * 30)

# Assignment 2

age = int(input("What\'s Your Age ?"))
print( "Hello Your Age Is Under 16, Some Articles Is Not Suitable For You" if age < 16 else  f"Hello Your Age Is {age}, All Articles Is Suitable For You" ) 
print("=" * 30)

# Assignment 3

fName =  input("What\'s Your Fisrt Name ?").strip().capitalize()
lName  =  input("What\'s Your Last Name ?").strip().capitalize()

print(f"Hello {fName} {lName:.1s}.")
print("=" * 30)


# Assignment 4


email =  input("What\'s Your Email ?").strip().capitalize()
pos = email.index("@")
pos_dot = email.index(".")

print(f"Your Name Is {(email[:pos])}\nEmail Service Provider Is {email[pos+1:pos_dot]}\nTop Level Domain Is {email[pos_dot+1 : ]}")




