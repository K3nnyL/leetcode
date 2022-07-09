import heapq
class Solution:
    def lastStoneWeight(self, stones):
        heap = []
        print(list(map(lambda x:heapq.heappush(heap,-x),stones)))
     #   for i in stones:
      #      heapq.heappush(heap,-1*i)
        while len(heap) > 1 and heap[0]!= 0:  
                heapq.heappush(heap,heapq.heappop(heap) - heapq.heappop(heap))
        return -heap[0]
        
if __name__ == '__main__':
    # begin
    s = Solution()
    Answer = s.lastStoneWeight([2,7,4,1,8,1,1])
    print(Answer)