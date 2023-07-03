def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"


print(greet('Daniel', 'Daniel'), 'Hello boss')
print(greet('Greg', 'Daniel'), 'Hello guest')

# Another Solution

# def greet(name, owner):
#     return f"Hello {'boss' if name == owner else 'guest'}"

# greet=lambda n,o:'Hello '+'gbuoessst'[n==o::2]

# def greet(a, b): return f"Hello {['guest','boss'][a==b]}"
# print(greet("moaz","moaz"))
