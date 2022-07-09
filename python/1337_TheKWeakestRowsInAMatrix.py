class Solution:
    def kWeakestRows(self, mat, k):
        '''
        d = []
        res = []
        for i in range(len(mat)):
            d.append([mat[i].count(1),i])
        d.sort()
        for i in d[:k]:
            res.append(i[1])
        return res
        '''
        res = []
        row,soldiers = len(mat),len(mat[0])
        for j in range(soldiers):
            for i in range(row):
                print(mat[i][j])
                if mat[i][j] == 0:
                    if i not in res:
                        res.append(i)
                if len(res) == k:
                    break
        if res == []:
            res = [0]
        return res

if __name__ == '__main__':
    # begin
    s = Solution()
    Answer = s.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]],3)
    print(Answer)
            
            
        
            