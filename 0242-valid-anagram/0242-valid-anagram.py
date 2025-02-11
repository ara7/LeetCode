class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_1 = {}
        dict_2 = {}
        for i in s:
            dict_1[i] = dict_1.get(i, 0) + 1 
        for j in t:
            dict_2[j] = dict_2.get(j, 0) + 1 
        print(dict_1)
        print(dict_2)
        if(dict_1.items() == dict_2.items()):
            return True
        return False


        