class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        found_chars = {}
        found_chars_t = {}

        for c in s:
            if c not in found_chars:
                found_chars[c] = 1
            found_chars[c] += 1
        
        for c in t: 
            if c not in found_chars_t:
                found_chars_t[c] = 1
            found_chars_t[c] += 1

        if found_chars == found_chars_t:
            return True
        return False

        
            