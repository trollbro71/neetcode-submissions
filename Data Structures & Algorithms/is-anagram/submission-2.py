class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        if len(s) != len(t):
            return False
        
        for letter in range(len(s)):
            s_dict[s[letter]] = 1 + s_dict.get(s[letter], 0)
            t_dict[t[letter]] = 1 + t_dict.get(t[letter], 0)
        return s_dict == t_dict