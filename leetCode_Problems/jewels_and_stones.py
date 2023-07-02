class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for letter in jewels:
            count += stones.count(letter)
        return count
    
jewels = "z"
stones = "ZZ"
count = 0
for letter in jewels:
    count += stones.count(letter)
print(count)

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Input: jewels = "z", stones = "ZZ"
# Output: 0