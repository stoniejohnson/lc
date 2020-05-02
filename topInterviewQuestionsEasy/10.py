from typing import List

class Solution(self, board: List[List[str]]) -> bool:
    def notInRow(arr, row):
        st = set()
        for i in range(0, 9):
            if arr[row][i] in st:
                return False

            if arr[row][i] != '.':
                st.add(arr[row][i])
        return True

    def notInCol(arr, col):
        st = set()
        for i in range(0, 9):
            if 
