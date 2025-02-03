class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subseq_len = 0
        
        for i in range(len(t)):
            if (subseq_len <= len(s)-1):
                if t[i] == s[subseq_len]:
                    subseq_len += 1
        return len(s) == subseq_len


        