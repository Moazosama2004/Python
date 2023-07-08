# Assignment 1

num = input("Add Your Number ")

if (len(num) > 1):
    raise IndexError(f"Only One Character Allowed")
else :
    if (65 <= ord(num) and ord(num) <= 90) or  (97 <= ord(num) and ord(num) <= 122):
        raise Exception(f"Only Numbers Allowed")
    else :
        if (int(num) > 0) :
            print(f"The Number Is {num}")
        else :
            raise ValueError(f"Number Must Be Larger Than 0")

print("=" * 30)
# Assignment 2
try:
    letter = input("Add Letter From A to Z ").strip()

    if (len(letter) > 1):
        raise IndexError()
    else:
        if (not (65 <= ord(letter) and ord(letter) <= 90)):
            raise Exception()


except IndexError:
    print(f"You Must Write One Character Only")

except Exception:
    print(f"The Letter Not In A - Z")

else:
    print(f"You Typed {letter}")

print("=" * 30)

# Assignment 3

def calculate(num1, num2) -> int:
    return num1 + num2


print(calculate(20, 30))


# print(ord("a"))
# print(ord("z"))
