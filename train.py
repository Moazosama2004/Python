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
import pyfiglet
import termcolor
import sys
arr = ["Burn" , "Out" , "Wallahe"]
for i in arr :
    print(termcolor.colored(pyfiglet.figlet_format(i) , color= "red"))

# print(termcolor.colored(pyfiglet.figlet_format("3la Zepe\n"), "green"))
# print(termcolor.colored(pyfiglet.figlet_format("Ya 3amer"), "green"))
