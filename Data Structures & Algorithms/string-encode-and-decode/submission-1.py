class Solution:

    def encode(self, strs: List[str]) -> str:
        ans= ""
        for i in strs:
            ans+= str(len(i)) + "$" + i
        return ans

    def decode(self, s: str) -> List[str]:
        ans_array=[]
        i=0
        while i < len(s):
            j=i
            while s[j] != "$":
                j+=1
            l = int(s[i:j]) #length of string

            ans_array.append(s[j+1:j+1+l])

            i=j+1+l
        
        return ans_array
        
