class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_dictionary = defaultdict(list)
        for s in strs:
            alphabets_count = [0] * 26

            for c in s:
                alphabets_count[ord(c) - ord('a')] += 1
        
            final_dictionary[tuple(alphabets_count)].append(s)
        return list(final_dictionary.values())

