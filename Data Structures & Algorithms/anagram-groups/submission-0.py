class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}
        for string in strs:
            sortedString = ''.join(sorted(list(string)))
            if sortedString not in dic:
                dic[sortedString] = [string]
            else:
                dic[sortedString].append(string)

        res = [x for x in dic.values()]
            
        return res