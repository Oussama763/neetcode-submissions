class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = "".join([char for char in s if "a" <=char<="z" or "A"<=char<="Z" or "0" <=char<= "9"])
        return s_new.lower() == s_new[::-1].lower()