class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     #trying with hash-data structure
     #trying hs
     hash_of_nums=set(nums)
     if len(nums) == len(hash_of_nums):
        return False
     else:
        return True