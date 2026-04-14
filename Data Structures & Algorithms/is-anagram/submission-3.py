class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #first edge case 

        if len(s) != len(t):
            return False


        #now have to create a hash-map for s and t
        S_hash_map = {}

        for i in s:
            if i in S_hash_map:
                S_hash_map[i] += 1
            else :
                S_hash_map[i] = 1

        T_hash_map = {}
        for j in t:
            if j in T_hash_map:
                T_hash_map[j]+=1
            else:
                T_hash_map[j]=1
        

        if T_hash_map == S_hash_map:
            return True
        else :
            return False


        
        