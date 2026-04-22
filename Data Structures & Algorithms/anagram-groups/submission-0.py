class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resDict= defaultdict(list)
        for i in strs:
            count = [0]*26
            for j in i:
                count[ord(j)-97] += 1
            resDict[tuple(count)].append(i)
        return list(resDict.values())