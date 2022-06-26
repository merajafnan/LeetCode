# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        s = s.split()
        return (len(s[-1]))