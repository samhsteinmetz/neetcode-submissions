class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ret = 0
        for word in words:
            count = Counter(chars)
            total = 0
            for char in word:
                if char not in count:
                    break
                count[char] -= 1
                if count[char] < 0:
                    break
                total += 1
            if total == len(word):
                ret+=len(word)

        return ret
                
            
            
                
            

        