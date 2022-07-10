import heapq
class Solution:
    def halveArray(self, nums):
        cout = 0
        target = sum(nums)/2
        mheap = []
        for i in nums:
            heapq.heappush(mheap,-i)
        while target>0:
            x = heapq.heappop(mheap)/2
            target = target + x
            heapq.heappush(mheap,x)
            cout += 1
        return cout
        

        
if __name__ == '__main__':
    # begin
    s = Solution()
    Answer = s.halveArray([5,19,8,1])
    print(Answer)