# 6.2.24-3
class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        aDict = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
                 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        for k, v in aDict.items():
            result += (num//k)*v
            num %= k
        return result
