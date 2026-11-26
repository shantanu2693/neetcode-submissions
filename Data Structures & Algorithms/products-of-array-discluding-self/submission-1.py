class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_list = [1] * len(nums)
        for i in range(1,len(nums),1):
            prefix_list[i] = prefix_list[i-1] * nums[i-1]
        
        suffix_list = [1] * len(nums)
        for j in range(len(nums)-2,-1,-1):
            suffix_list[j] *= suffix_list[j+1] * nums[j+1]

        result = [None] * len(nums)
        for k in range(len(nums)):
            result[k] = prefix_list[k]*suffix_list[k]

        return result


    
