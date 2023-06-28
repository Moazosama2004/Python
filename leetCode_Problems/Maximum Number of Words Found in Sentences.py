# class Solution:
#     def mostWordsFound(self, sentences: List[str]) -> int:
#         max_words = 0
#         for sentence in sentences:
#             if max_words < len(sentence.split(" ")) :
#                 max_words = len(sentence.split(" "))
#         else :
#             return max_words

# sentences = ["please wait", "continue to fight", "continue to win"]
# max_words = 0
# for sentence in sentences:
#     if max_words < len(sentence.split(" ")) :
#         max_words = len(sentence.split(" "))
# else :
#     print(max_words)

# Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# Output: 6
# Explanation: 
# - The first sentence, "alice and bob love leetcode", has 5 words in total.
# - The second sentence, "i think so too", has 4 words in total.
# - The third sentence, "this is great thanks very much", has 6 words in total.
# Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.

