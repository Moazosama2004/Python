def binary_pyramid(m,n):
    sum = 0
    for i in range(m,n+1) :
        sum += int(bin(i)[2:])
    return bin(sum)[2:]

print(binary_pyramid(1,4))


# Another Solution 

# def binary_pyramid(m,n):
#     return bin(sum(int(bin(i)[2:]) for i in range(m, n+1)))[2:]


