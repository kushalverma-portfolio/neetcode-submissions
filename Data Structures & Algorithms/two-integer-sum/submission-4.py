class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict ={}
        answer = []
        for i in range(len(nums)):

            
            if nums[i] in dict: return [dict[nums[i]],i]
            else:
                diff = target - nums[i]
                dict[diff]= i
