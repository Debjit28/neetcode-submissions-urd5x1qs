class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #optimal soulution after Yt
        ans=[1]*len(nums)#to create array of exactly same size as nums
        prefix=1
        for i in range(0,len(nums)):
            ans[i]=prefix

            prefix*=nums[i]

        postfix=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=postfix

            postfix*=nums[i]
        
        return ans