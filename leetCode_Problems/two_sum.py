from ast import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetlst = []
        indexone = 0
        while (indexone < len(nums)):
            indextwo = indexone + 1
            while (indextwo < len(nums)):
                if target == nums[indexone] + nums[indextwo]:
                    targetlst.append(indexone)
                    targetlst.append(indextwo)
                    break
                else:
                    indextwo += 1
            indexone += 1

        return targetlst

nums = [2, 7, 11, 15]
target = 9
targetlst = []

indexone = 0
while (indexone < len(nums)):
    indextwo = indexone + 1
    while (indextwo < len(nums)):
        if target == nums[indexone] + nums[indextwo]:
            targetlst.append(indexone)
            targetlst.append(indextwo)
            break
        else:
            indextwo += 1
    indexone += 1

print(targetlst)


# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].