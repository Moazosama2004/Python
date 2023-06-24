# Assignment 1
name = "Moaz"
age = 19
country = "Egypt"

print("Hello \'%s\', How You Doing \\ \"\"\" Your Age Is \" %d \"\" + And Your Country Is: %s" %(name, age, country))
print("=" * 30)

# Assignment 2

print("Hello \'%s\', How You Doing \\\n\"\"\" Your Age Is \" %d \"\" +\nAnd Your Country Is: %s" %(name, age, country))
print("=" * 30)

# Assignment 3

name = 'Elzero'
print("Second Letter Is : " + name[1])
print("Third Letter Is : " + name[2])
print("Last Letter Is : " + name[-1])
print("=" * 30)

# Assignment 4

print(name[1:4])
print(name[::2])
print(name[-2::-2])
print("=" * 30)

# Assignment 5

name = "#@#@Elzero#@#@"

print(name.strip("#@"))
print("=" * 30)

# Assignment 6

num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))
print("=" * 30)

# Assignment 7

name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20, "@"))
print(name_two.rjust((7+len(name_two)), "@"))
print("=" * 30)

# Assignment 8

name_one = "OSamA"
name_two = "osaMA"

print(name_one.swapcase())
print(name_two.swapcase())
print("=" * 30)

# Assignment 9

msg = "I Love Python And Although Love Elzero Web School"

print(msg.count("Love"))
print("=" * 30)

# Assignment 10

name = "Elzero"

print(name.index("z"))
print("=" * 30)

# Assignment 11

msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace("<3", "Love" , 1))
print("=" * 30)

# Assignment 12

print(msg.replace("<3", "Love"))
print("=" * 30)

# Assignment 13

name = "Osama"
age = 38
country = "Egypt"

print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")
