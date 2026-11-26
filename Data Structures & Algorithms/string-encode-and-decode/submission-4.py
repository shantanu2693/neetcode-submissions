import json

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_dict = defaultdict(list)

        for i,s in enumerate(strs):
            if (len(s) == 0):
                encoded_dict[i].append("")
            for char in s:
                encoded_dict[i].append(char)
        return json.dumps(encoded_dict)

    def decode(self, s: str) -> List[str]:

        list_of_strings = []
        encoded_dict = json.loads(s)
        for k,v in encoded_dict.items():
            list_of_strings.append("".join(v))

        return list_of_strings
