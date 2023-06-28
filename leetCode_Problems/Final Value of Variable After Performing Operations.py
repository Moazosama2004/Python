# class Solution:
#     def finalValueAfterOperations(self, operations: List[str]) -> int:
#         X = 0
#         for o in operations :
#             if o == "--X" or o == "X--" :
#                 X -= 1        
#             elif o == "++X" or o == "X++" :
#                 X += 1 
#         else :
#             return X

# operations = ["++X","++X","X++"]
# X = 0
# for o in operations :
#     if o == "--X" or o == "X--" :
#         X -= 1        
#     elif o == "++X" or o == "X++" :
#         X += 1 
# else :
#     print(X)


# Input: operations = ["++X","++X","X++"]
# Output: 3
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# ++X: X is incremented by 1, X = 0 + 1 = 1.
# ++X: X is incremented by 1, X = 1 + 1 = 2.
# X++: X is incremented by 1, X = 2 + 1 = 3.