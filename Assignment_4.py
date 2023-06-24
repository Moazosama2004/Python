# Assignment 1

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0])
print(friends[-5])
print(friends[-1])
print(friends[4])
print(friends[len(friends)-1])
print("=" * 30)

# Assignment 2
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[::2])
print(friends[1::2])
print("=" * 30)

# Assignment 3

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[1:4])
print(friends[len(friends)-2:len(friends)])
print("=" * 30)

# Assignment 4

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

friends[3:5] = ["Elzero", "Elzero"]
print(friends)
print("=" * 30)

# Assignment 5

friends = ["Osama", "Ahmed", "Sayed"]

friends.insert(0, "Nasser")
print(friends)

friends.append("Salem")
print(friends)
print("=" * 30)

# Assignment 6

friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends[:2] = []
print(friends)
friends.pop(-1)
print(friends)
print("=" * 30)

# Assignment 7

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends.extend(employees)
friends.extend(school)
print(friends)
print("=" * 30)

# Assignment 8

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
print("=" * 30)

# Assignment 9

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

print(len(friends))
print("=" * 30)

# Assignment 10

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[4][0])
print(technologies[4][-1])

