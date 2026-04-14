class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans_arr=[]
        for i in range(0,len(nums)):
            prod=1
            for j in range(0,len(nums)):
                if i!=j:
                    prod*=nums[j]
            ans_arr.append(prod) 
        return ans_arr