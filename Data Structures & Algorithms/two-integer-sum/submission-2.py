class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count_dict = defaultdict(int)

        for i,n in enumerate (nums):
            count_dict[n] = i

        for i,n in enumerate (nums):
            diff = target - n
            if (diff in count_dict and count_dict[diff] != i):
                return [i, count_dict[diff]]
        
        return []