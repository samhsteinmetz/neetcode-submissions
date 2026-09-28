class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if '.' == curr:
                    continue
                else:
                    if curr not in rows[i]:
                        rows[i].add(curr)
                    else:
                        return False
                    if curr not in cols[j]:
                        cols[j].add(curr)
                    else:
                        return False
                    if curr not in boxes[((i // 3), (j//3))]:
                        boxes[((i // 3), (j//3))].add(curr)
                    else:
                        return False
        return True
                    
                    

