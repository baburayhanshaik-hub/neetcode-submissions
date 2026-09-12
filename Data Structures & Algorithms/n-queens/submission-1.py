import copy 
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        visited = [["."]*n for i in range(n)]
        ans = []
        def check(line,i):
            for v in range(0,line):
                if visited[v][i]=='Q':
                    return
            up, left, right = line,0,0
            while True:
                up-=1
                left-=1
                right+=1
                if up<0:
                    return True
                if i+left>=0 and visited[up][i+left]=="Q":
                    return False
                if i+right<n and visited[up][i+right]=="Q":
                    return False
        def func(line):
            nonlocal ans
            if line>=n:
                temp = []
                for i in copy.deepcopy(visited):
                    temp.append("".join(i))
                ans.append(temp)
                return
            for i in range(0,n):
                if check(line,i):
                    visited[line][i]="Q"
                    func(line+1)
                    visited[line][i]="."
        func(0)
        return ans