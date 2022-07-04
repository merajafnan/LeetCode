# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
# Input: s = "egg", t = "add"
# Output: true

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        s1 = {}
        t1 = {}

        for i in range(len(s)):
            if s[i] not in s1:
                s1[s[i]] = i
            if t[i] not in t1:
                t1[t[i]] = i
            if s1[s[i]] != t1[t[i]]:
                return False
        return True