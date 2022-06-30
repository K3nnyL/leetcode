class Solution:
    def twoSum(self,nums,target):
        hashmap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[n] = i    

        
if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.twoSum([2,7,11,15],9))