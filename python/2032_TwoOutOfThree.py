class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        
        set1 = set(nums1) & set(nums2)
        set2 = set(nums1) & set(nums3)
        set3 = set(nums3) & set(nums2)
        print(set1,set2,set3)
        
        return list(set1 | set2 | set3)
        

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.twoOutOfThree([1,1,3,2],[2,3],[3]))