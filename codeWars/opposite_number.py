def opposite(number):
    return -number

print(opposite(1),-1)
print(opposite(25.6), -25.6)
print(opposite(0), 0)
print(opposite(1425.2222), -1425.2222)
print(opposite(-3.1458), 3.1458)
print(opposite(-95858588225),95858588225)

# Another Solution
def opposite(number):
    
#fastest solution returned 94ms with parens around multiplication 87ms without for results
    return number - number * 2 

#middle solution returned 109ms time period for result
#    return number * -1
#slowest solution returned 150ms time period for result
#    return -number
