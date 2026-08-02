class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #optimal soln...use row track and col track...jaha pr bhi 0 mile suke row and col index ko -1 pr set kr dnege aur phir baad me jaha jaha -1 rahega usko zero me convert kr denge
        r=len(matrix)
        c=len(matrix[0])
        row_track=[0 for _ in range(r)]
        col_track=[0 for _ in range(c)]

        #zero dundho aur row_track nd col_track ko -1 pr set kro
        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j]==0:
                    row_track[i]=-1
                    col_track[j]=-1
        # ab jaha pr -1 h udr zero krdo 
        for i in range(0,r):
            for j in range(0,c):
                if row_track[i]==-1 or col_track[j]==-1:
                    matrix[i][j]=0