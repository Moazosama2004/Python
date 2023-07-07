# Assignment 1
from PIL import Image
my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for item1, item2 in zip(my_list, my_tuple):
    my_data.append(item1)
    my_data.append(item2)

final_string = "".join(my_data).capitalize()
print(final_string)  # Elzero

print('=' * 30)

# Assignment 2

my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    if (type(item1) == int):
        continue
    my_data.append(item1)

final_string = "".join(my_data).capitalize()
print(final_string)  # Elzero

print('=' * 30)

# Assignment 3

# myImage = Image.open("C:\Python\elzero-pillow.png")
# myImage.show()

# box = (400, 0, 800, 400)
# myL = myImage.crop(box)
# myL.show()
# MLGray = myL.convert("L")
# MLGray.show()

# box1 = (0, 400, 1200, 800)
# myL1 = myImage.crop(box1)
# myL1.show()
# MLGray1 = myL1.convert("L")
# MLGray1.show()
# MLRotating = MLGray1.rotate(angle=180)
# MLRotating.show()


# Assignment 4

def say_hello_to (name) :
  """
  parameter(someone) => Person Name
  Function To Say Hello To Anyone
  """
  return f"Hello {name}"

print(say_hello_to("Osama")) # "Hello Osama"

print(say_hello_to.__doc__)
print(help(say_hello_to))

# Function Doc String Output
"parameter(someone) => Person Name"
"Function To Say Hello To Anyone"
print("=" * 30)

# Assignment 5

"""
_summary_
"""

myFriends = ["Ahmed", "Osama", "Sayed"]

def say_hello (some_peoples) -> list:
    """_summary_
    Args:
        some_peoples (_type_): _description_

    Returns:
        list: _description_
    """
    for someone in some_peoples:
        print(f"Hello {someone}")

say_hello(myFriends)