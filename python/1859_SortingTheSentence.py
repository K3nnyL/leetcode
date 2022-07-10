


class Solution:
    def sortSentence(self, s: str) -> str:
        lst = s.split()
        d = ["" for i in lst]
        for word in lst:
            d[int(word[-1])-1]= word[:-1] 
        res =" ".join(d)
        return res



if __name__ == '__main__':
    # begin
    s = Solution()
    Answer = s.sortSentence("is2 sentence4 This1 a3")
    print(Answer)