class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        if any(v > 1 for v in d.values()):
            return True
        else:
            return False