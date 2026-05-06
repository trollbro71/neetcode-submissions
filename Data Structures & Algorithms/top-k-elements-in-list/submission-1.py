class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # hash table
        freq = [[] for i in range(len(nums) + 1)] # the buckets

        for num in nums: # iterate the array
            count[num] = 1 + count.get(num, 0) #get the freq of each number in the array 
 

        for num, cnt in count.items():
            freq[cnt].append(num) # bucket is # of items: [number]
        res = []

        for i in range(len(freq) - 1, 0, -1): # iterate the bucket backwards 
            for num in freq[i]: 
                res.append(num) # if the value exists append it to results
                if len(res) == k:  # This stops the for loop 
                    return res # return 