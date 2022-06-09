# Input: s = "anagram", t = "nagaram"
# Output: true

# Input: s = "rat", t = "car"
# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)