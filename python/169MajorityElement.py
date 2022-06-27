class Solution:
    def majorityElement(self, nums):
        count = 0
        max = 0
        for x in nums:
            if count==0:
                max = x
                count = 1
            elif max == x:
                count +=1
            else:
                count -=1
        return max

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.majorityElement([2,2,1,1,1,2,2]))