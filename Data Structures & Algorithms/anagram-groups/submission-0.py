class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_anagram={}#empty map
        for i in strs:
            key = "".join(sorted(i))

            if key not in grp_anagram:
                grp_anagram[key]=[]#key:0 i.e no elements are to corressponding keys
            grp_anagram[key].append(i)#if the key exist then pls append this 


        return list(grp_anagram.values())
         