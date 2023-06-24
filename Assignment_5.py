# Assignment 1

myTuple = "Moaz",
print(myTuple)
print(type(myTuple))
print("=" * 30)

# Assignment 2

friends = ("Osama", "Ahmed", "Sayed")

friends_list = list(friends)
friends_list[0] = "Elzero"
friends = tuple(friends_list)

print(friends)
print(type(friends))
print(len(friends))
print("=" * 30)

# Assignment 3

nums = (1, 2, 3)
letters = ("A", "B", "C")

nums = nums + letters
print(f"nums_and_letters_one = {nums}")
print(len(nums))
print("=" * 30)

# Assignment 4

my_tuple = (1, 2, 3, 4)

a,b,_,c = my_tuple
print(a)
print(b)
print(c)
