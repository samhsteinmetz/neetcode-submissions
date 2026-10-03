class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(list(ransomNote))
        
        for char in magazine:
            if char in counter and counter[char] != 0:
                counter[char]-=1
                if counter[char] < 0:
                    print(char)
                    return False
        
        s = 0
        for key, val in counter.items():
            s += val
        print(counter)
        if s>0:
            return False
        return True