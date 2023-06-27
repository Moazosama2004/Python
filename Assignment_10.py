# Assignment 1

num = int(input("Enter a number Here : ").strip())
count = 0

if num > 0:
    while num > 0:
        num -= 1
        if num == 0:
            break
        if num == 6:
            continue
        print(num)
        count += 1
    print(f"{count} Numbers Printed Successfully.")

else:
    print(f"Number {num} Is Not Larger Than 0")
print("=" * 30)

# Assignment 2

friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
discarded = 0

index = 0
while index < len(friends) :
    if friends[index] != friends[index].lower() :
        print(friends[index])
        index+=1
    else :
        discarded += 1
        index += 1
        continue
else : 
    print(f"Friends Printed And Ignored Names Count Is {discarded}")
print("=" * 30)

# Assignment 3

skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:
    skills.reverse(); print(skills.pop())
print("=" * 30)

# Assignment 4

print("#" * 50)
print(" Hello , You Can Now ADD your Friends ".center(50 , "#"))
print("#" * 50)


my_friends = []
max_friends = 4

while max_friends > 0 : 
    
    name = input("What\'s Name you Want be Added : ").strip()

    if name == name.upper() :
        print("Invalid Name")

    elif name == name.lower() :
        name.capitalize()
        print(f"Friend {name} Added => 1st Letter Become Capital")
        my_friends.append(name)
        max_friends -= 1

    elif name == name.capitalize() :
        print(f"Friend {name} Added")
        my_friends.append(name)
        max_friends -= 1

    else : 
        print("Enter A valid Name Please : ")
        
    print(f"Names Left in List Is {max_friends}")

else : 
    print("List Is Full Now")
    print(my_friends)




