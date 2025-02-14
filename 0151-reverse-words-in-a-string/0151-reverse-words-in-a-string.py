class Solution:
    def reverseWords(self, s: str) -> str:
        #I want to use rescursion
        s_space_removed = s.split(" ")
        s_space_removed = [i for i in s_space_removed if len(i)!=0]
        if len(s_space_removed) == 1:
            return s_space_removed[0]
        else:
            return s_space_removed[-1] + " " + self.reverseWords(" ".join(s_space_removed[:-1])) #convert list to str before sending to recursion
        

        