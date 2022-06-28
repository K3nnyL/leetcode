class Solution:
    def containsDuplicate(self, nums):
        map = {}
        for i in nums:
            if i in map:
                return True
            else:
                map[i] = None
        return False

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.containsDuplicate([1,2,3,4]))

