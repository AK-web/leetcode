class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = []

        for num in set(nums):
            arr.append([nums.count(num), num])

        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])

        return res