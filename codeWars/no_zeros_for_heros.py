def no_boring_zeros(n):
    number = str(n)
    i = -1 
    while(-1 > -(len(number))) :
        if number[i] == "0" :
            i-=1
        else :
            break
    a = list(reversed(number[i::-1]))
    return int("".join(a))


n = "10101010"
i = -1 
while(-1 > -(len(n))) :
    if n[i] == "0" :
        i-=1
    else :
        break
last_number = int("".join(list(reversed(n[i::-1]))))
print(last_number)


# Another Solution With rstrip()

# def no_boring_zeros(n):
#     return int(str(n).strip("0")) if n else n