class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        k=len(strs)
        dp=[[[-1 for i in range(n+1)] for j in range(m+1)] for k in range(k+1)]
        def dfs(k1,m1,n1):
            if k1==0 or k1==k+1 or (m1==0 and n1==0):
                dp[k1][m1][n1]=0
                return 0
            if(dp[k1][m1][n1]==-1):
                countOnes=strs[k1-1].count('1')
                countZeros=strs[k1-1].count('0')
                res=dfs(k1-1,m1,n1)
                if countZeros<=m1 and countOnes<=n1:
                    res=max(res,dfs(k1-1,m1-countZeros,n1-countOnes)+1)
                dp[k1][m1][n1]=res
            return dp[k1][m1][n1]
        
        return dfs(k,m,n)