class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute force approach
        if len(s)!= len(t):
            return False

        if len(s) == 0 and len(t) == 0:
            return False
        

        s_list = list(s)
        t_list = list(t)

        s_list.sort()
        t_list.sort()

        if s_list == t_list:
            return True
        
        else:
            return False

          