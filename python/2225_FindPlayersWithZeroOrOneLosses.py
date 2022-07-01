class Solution:

    def findWinners(self, matches):
        count = [[] for i in range(len(matches)+1)]
        temp = {}
        
        for w,l in matches:  # win = NothingChange , Lost = +1
            temp[w] = temp.get(w,0)
            temp[l] = 1+temp.get(l,0)
            
        for p,l in temp.items():
            count[l].append(p)

        
        return [sorted(count[0]),sorted(count[1])]
        

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.findWinners([[2,3],[1,3],[5,4],[6,4]]))
    s.findWinners([[2,3],[1,3],[5,4],[6,4]])

    
