class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_1 = {}
        dict_2 = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if s_char in dict_1:
                if dict_1[s_char] != t_char:
                    return False
            else:#establishing a new mapping
                if t_char in dict_2:#check if t_char already in dict_2
                    return False #already mapped
                dict_1[s_char] = t_char
                dict_2[t_char] = s_char
        return True
        