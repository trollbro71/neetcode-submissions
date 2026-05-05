class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_subset = {} 
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            key = tuple(count)
            if key not in hash_subset:
                hash_subset[key] = []
            hash_subset[key].append(word)
        return list(hash_subset.values())
