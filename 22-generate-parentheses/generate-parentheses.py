class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(lp,rp,s):
            if len(s)==2*n:
                res.append(s)
                return
            if lp<n:
                helper(lp+1,rp,s+'(')
            if rp<lp:
                helper(lp,rp+1,s+')')
        res=[]
        helper(0,0,'')
        return res