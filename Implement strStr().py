# Implement strStr().
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if haystack == 0 and needle == 0:
            return 0

        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1