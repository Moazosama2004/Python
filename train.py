# def century(year):
#     century = str(year)
#     if int(century[-1]) > 0:
#         century = int(century[0:2]) + 1
#     else:
#         century = century[0:2]
#     return century

# print(century(1705), 18, 'Testing for year 1705')
# print(century(1900), 19, 'Testing for year 1900')
# print(century(1601), 17, 'Testing for year 1601')
# print(century(2000), 20, 'Testing for year 2000')
# print(century(356), 4, 'Testing for year 356')
# print(century(89), 1, 'Testing for year 89')
# import pyfiglet
# import termcolor
# import sys
# arr = ["Burn", "Out", "Wallahe"]
# for i in arr:
#     print(termcolor.colored(pyfiglet.figlet_format(i), color="red"))

# print(termcolor.colored(pyfiglet.figlet_format("3la Zepe\n"), "green"))
# print(termcolor.colored(pyfiglet.figlet_format("Ya 3amer"), "green"))
# print(5+3)

# def maiin (n1 , n2 ) :
#     print(n1 + n2)
#     return n1 + n2

# result = maiin(5 , 10)
# print(result)



# def reverse_string(my_string):
#     for letter in reversed(my_string) :
#         yield letter

# # Reverse The String
# for c in reverse_string("Elzero"):
#     print(c,end=" ")

# Create Your Decorator Here

def myDecorat (func) :
    def nestedfunc () :
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