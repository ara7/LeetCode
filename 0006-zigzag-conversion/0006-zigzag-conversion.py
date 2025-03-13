class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        res = ""
        for r in range(numRows): #O(N)
            increment = 2*(numRows - 1)
            # inside loop can't possible execute more times than the number of characters that were given in the input. Not visiting the same character twice because our incrementer could be a really large value 
            for i in range(r,len(s), increment):
                res += s[i]
                #i + increment - 2 * r : index of position that we dont want to fotget for middle rows
                #i + increment - 2 * r < len(s) to make sure it is in bounds
                if (r>0 and r<numRows - 1 and i + increment - 2 * r < len(s)):
                    res += s[i + increment - 2 * r]
        return res

        