class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum = 0
        for i in range(len(mat)):
            sum += mat[i][i]
            if i!= len(mat)//2 and len(mat)%2!=0:
                sum += mat[i][-i-1]
            if len(mat)%2==0:
                sum += mat[i][-i-1]
        return sum