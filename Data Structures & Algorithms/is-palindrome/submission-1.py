class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_string = ("".join(char for char in s if char.isalnum())).lower()
        l = len(stripped_string)
        reversed_stripped_string = ""
        for i in range(l-1,-1,-1):
            reversed_stripped_string = reversed_stripped_string + stripped_string[i]

        if (stripped_string == reversed_stripped_string):
            return True
        else:
            return False

