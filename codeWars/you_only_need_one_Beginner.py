def check(seq, elem):
    return list(seq).count(elem) > 0

print(check([50,20,80,123] , 3))

# Another Solution 

# def check(seq, elem):
#     return elem in seq