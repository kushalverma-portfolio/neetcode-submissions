class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bool = False
        setList = set(nums)
        if len(nums) > len(setList) : bool = True
        return bool
        