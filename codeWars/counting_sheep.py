def count_sheeps(sheeps):
    for sheep in sheeps :
        try :
            if (int(sheep) == 1) :
                no_sheeps += 1
            else :
                continue
        except TypeError:
            continue
    return no_sheeps

# Another Solution 
# def count_sheeps(arrayOfSheeps):
#     return arrayOfSheeps.count(True)

# def count_sheeps(array_of_sheep):
#   # TODO May the force be with you
#   count = 0
#   for sheep in array_of_sheep:
#       if sheep:
#           count += 1 
#   return count


