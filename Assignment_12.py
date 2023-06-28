# Assignment 1

def calculate (n1 , n2 , procces = "a") :
    if procces.lower() == "add" or procces[0].lower() == "a" :
        return n1 + n2
    elif procces.lower() == "subtract" or procces[0].lower() == "s" :
        return n1 - n2
    elif procces.lower() == "multiply" or procces[0].lower() == "m" :
        return n1 * n2
    else :
        return "Please Enter A valid Progress"

# Tests
print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30

print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200
print("=" * 30)

# Assignment 2

def addition(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    else:
        return sum
    
# Tests
print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160

print("=" * 30)

# Assignment 3

def show_skills (name , *skills) :
    if len(skills) > 0 :
        print(f"Hello {name} Your Skills Is : ")
        for skill in skills :
            print(f"- {skill}")
    else : 
        print(f"\" Hello {name} You Have No Skills To Show \"")

show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")

print("=" * 30)

# Assignment 4

def say_hello (name = "Unknown" , age = "Unknown", country = "Unknown") :
    return f"Hello {name} Your Age Is {age} And You Live In {country}"

print(say_hello("Osama", 38, "Egypt"))
print(say_hello())

print("=" * 30)




