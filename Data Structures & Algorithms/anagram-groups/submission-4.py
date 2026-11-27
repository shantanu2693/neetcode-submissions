class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if (len(strs) == 0):
            return [[""]]

        if (len(strs) == 1):
            return [strs]

        count_dict = defaultdict(list)

        for i,string in enumerate(strs):
            count = [0]*26
            for c in string:
                count[ord(c) - ord('a')] += 1

            count_dict[tuple(count)].append(string)
        
        return [v for v in count_dict.values() if len(v) > 0]
        
