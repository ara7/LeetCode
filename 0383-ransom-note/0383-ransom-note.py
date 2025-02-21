class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #Use frequency maps
        ran_dict = {}
        mag_dict = {}

        for i in ransomNote:
            ran_dict[i] = ran_dict.get(i, 0) + 1

        for j in magazine:
            mag_dict[j] = mag_dict.get(j, 0) + 1

        for ran in ran_dict:
            if (ran in mag_dict) and ran_dict[ran]<= mag_dict[ran]:
                continue
            else:
                return False
                
        return True
        