class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)
        arr = [[] for i in range(len(nums)+1)]
        for n in nums:
            count_dict[n] += 1
        
        for key,value in count_dict.items():
            arr[value].append(key)

        result = []
        for i in range(len(arr) - 1,0,-1):
            for num in arr[i]:
                result.append(num)
                if (len(result) == k):
                    return result
        
