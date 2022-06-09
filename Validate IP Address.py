# Input: queryIP = "172.16.254.1"
# Output: "IPv4"
# Explanation: This is a valid IPv4 address, return "IPv4".

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ipv4 = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$')
        if ipv4.match(queryIP):
            return("IPv4")
        ipv6 = re.compile(r'^(([0-9a-f]{1,4}):){7}([0-9a-f]{1,4})$')
        if  ipv6.match(queryIP.lower()):
            return("IPv6")
        return("Neither")