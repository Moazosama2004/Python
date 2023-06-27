# Assignment 1

my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse=True)
count = 0
for num in my_nums:
    if num % 5 == 0:
        count += 1
        print(f"{count} => {num}")

else:
    print("All Numbers Printed")

print("=" * 30)

# Assignment 2

for num in range(1 , 21) :
    if num == 6 or num == 8 or num ==12 :
        continue
    else :
        if num < 10 :
            print(str(num).zfill(2))
        else :
            print(num)
else:
    print("All Numbers Printed")

print("=" * 30)

# Assignment 3

my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}

total_points = 0

for key, value in my_ranks.items():
    if value == "A":
        point = 100
        
    elif value == "B":
        point = 80

    elif value == "C":
        point = 40

    print(f"My Rank in {key} Is {value} And This Equal {point} Points")
    total_points += point

else:
    print(f"Total Points Is {total_points}")

print("=" * 30)


#### This Case Print All keys , values for skills with out counting total points ####
# print(f"My Rank in {key} Is {value} And This Equal {100 if value == 'A' else 80 if value == 'B' else 40} Points")


# Assignment 4

students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

total_points = 0
point = 0 

for student_key , student_value in students.items() : 
    print("------------------------------")
    print(f" Student Name => {student_key}".center(25))
    print("------------------------------\n")
    for child_key , child_value in student_value.items() :
        if child_value == "A":
            point = 100

        elif child_value == "B":
            point = 80

        elif child_value == "C":
            point = 40

        elif child_value == "D":
            point = 20

        print(f"- {child_key} => {point} Points")
        total_points += point

    else :
        print(f"\nTotal Points For Ahmed Is {total_points}\n")  
        total_points = 0 




