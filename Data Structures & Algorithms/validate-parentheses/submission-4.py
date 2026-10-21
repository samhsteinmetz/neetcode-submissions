class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {'}':'{', ')':'(', ']':'['}
        deq = []
        for char in s:
            # if open then push the close
            if char in closeToOpen:
                if deq and deq[-1] == closeToOpen[char]:
                    deq.pop()
                else:
                    return False
            else:
                deq.append(char)




        return False if deq else True

        

        