class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_val = {'I':1, 'V':5, 'X':10,'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0

        for i in range(len(s)-1):
            if roman_to_val[s[i]]< roman_to_val[s[i+1]]:
                result -= roman_to_val[s[i]]
            else:
                result += roman_to_val[s[i]]
        return result+roman_to_val[s[-1]]

        