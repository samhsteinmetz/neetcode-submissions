class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # dic = {}
        # for string in strs:
        #     sortedString = ''.join(sorted(list(string)))
        #     if sortedString not in dic:
        #         dic[sortedString] = [string]
        #     else:
        #         dic[sortedString].append(string)

        # res = [x for x in dic.values()]
            
        # return res

        dic = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            dic[tuple(count)].append(s)
        
        res = [x for x in dic.values()]
        return res

