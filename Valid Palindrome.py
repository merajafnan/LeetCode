# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.



s = ''.join(i for i in s.lower() if i.isalnum())
return True if s == s[::-1] else False

#
# if s == ' ':
#     print('true')
#
# s1 = []
# for i in s:
#     if i.isalnum():
#         s1.append(i)
# print(s1)
# s1 = ''.join(s1)
# s1 = s1.lower()
# print(s1)
# s = s1[::-1]
# if s1 == s:
#     print('true')
# else:
#     print('false')


