import heapq
class Solution:
    def maximumProduct(self, nums, k):
        heap = []
        modu = 10**9+7
        for num in nums:
            heapq.heappush(heap,num)
        for i in range(k):
            x = heapq.heappop(heap) + 1
            heapq.heappush(heap,x)
        res = 1
        for i in heap:
            res = (res * i)%modu
        return res
        
        
        

if __name__ == '__main__':
    # begin
    s = Solution()
    Answer = s.maximumProduct([0,4],5)
    print(Answer)