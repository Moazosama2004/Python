# Assignment 1

def reverse_string(my_string):
    for letter in reversed(my_string):
        yield letter


for c in reverse_string("Elzero"):
    print(c, end=" ")
print("\n")
print('=' * 30)
print("\n")

# Assignment 2


def myDecorat(func):
    def nestedfunc():
        print("Sugar Added From Decorators")
        func()
        print("####################")

    return nestedfunc


@myDecorat
def make_tea():
    print("Tea Created")


@myDecorat
def make_coffe():
    print("Coffe Created")


make_tea()
make_coffe()

# Needed Output

"Sugar Added From Decorators"
"Tea Created"
"####################"
"Sugar Added From Decorators"
"Coffe Created"
"####################"
