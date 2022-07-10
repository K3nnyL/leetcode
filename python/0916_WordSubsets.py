class Solution(object):
    def wordSubsets(self, A, B):
        def lettercheck(word):
            ans = [0]*26
            for letter in word:
                ans[ord(letter)-ord("a")] +=1
            return ans
        bcount = [0]*26
        res = []
        for b in B:
            for i,c in enumerate(lettercheck(b)):
                bcount[i] = max(bcount[i],c)
        for a in A:
            if all(x>=y for x,y in zip(lettercheck(a),bcount)):
                res.append(a)
        return res




if __name__ == '__main__':
    # begin
    s = Solution()
    Answer = s.wordSubsets(["amazon","apple","facebook","google","leetcode"],["lo","eo"])
    print(Answer)