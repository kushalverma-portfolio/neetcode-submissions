class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resDict ={}
        answer = []
        for i in range(len(nums)):

            
            if nums[i] in resDict: return [resDict[nums[i]],i]
            else:
                diff = target - nums[i]
                resDict[diff]= i
