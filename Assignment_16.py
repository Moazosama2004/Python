# Assignment 1

# With Normal Usage => Function 

from functools import reduce


friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL", "lMoazl"]

def remove_chars(name):
    return name[1: -1]

cleaned_list = map(remove_chars, friends_map)
for name in cleaned_list:
    print(name)

print("=" * 15)

# With Lambda Function => Lambda

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL", "lMoazl"]

cleaned_list = map(lambda name : name[1: -1] , friends_map)
for name in cleaned_list:
    print(name)

print("=" * 30)

# Assignment 2

# With Normal Usage => Function 

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

def get_names (name) :
    return name[-1] == "m" 

names = filter(get_names , friends_filter)
for name in names :
    print(name)

print("=" * 15)

# With Lambda Function => Lambda

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

names = filter(lambda name : name[-1] == "m"  , friends_filter)
for name in names :
    print(name)

print("=" * 30)

# Assignment 3

# With Normal Usage => Function 

nums = [2, 4, 6, 2]

def multi (num1 , num2) :
        return num1 * num2

multiplcation  = reduce(multi , nums)
print(multiplcation)

# With Lambda Function => Lambda

nums = [2, 4, 6, 2]

multiplcation  = reduce(lambda num1 , num2 : num1 * num2  , nums)
print(multiplcation)

# ShortCut 
print(reduce(lambda num1 , num2 : num1 * num2  , [2, 4, 6, 2]))

print("=" * 30)

# Assignment 4

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
enum_skills = enumerate(reversed(skills) , 50) 
for counter , skill in  enum_skills:
    if type(skill) != str :
        continue
    else :
        print(f"{counter} - {skill}")

