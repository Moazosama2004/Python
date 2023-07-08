def update_light(current):
    l = ["green" , "yellow" , "red"]
    return l[(l.index(current) + 1) % len(l)] 

print(update_light('green'), 'yellow')
print(update_light('yellow'), 'red')
print(update_light('red'), 'green')
        