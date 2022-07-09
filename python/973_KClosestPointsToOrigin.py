import heapq
'''##with sorted
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst = []
        res = []
        for i in range(len(points)):
            distance = points[i][0]**2 + points[i][1]**2
            lst.append([distance,i])
        lst.sort()
        for i in range(k):
            res.append(points[lst[i][1]])
        return res
        

        
'''
class Solution:
    def kClosest(self, points, k):
        heap = []
        
        for i in points:
            distance = i[0] ** 2 + i[1] ** 2
            if len(heap) >k-1:
                heapq.heappushpop(heap, [-distance, i])
            else:
                heapq.heappush(heap, [-distance, i])

        return [i for [distance, i] in heap]


if __name__ == '__main__':
    # begin
    s = Solution()
    Answer = s.kClosest([[3,3],[5,-1],[-2,4]],2)
    print(Answer)       