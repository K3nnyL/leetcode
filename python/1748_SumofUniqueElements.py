class Solution:
    def sumOfUnique(self, nums):
        
        total = 0
        dict ={}
        for i in nums:
            if i in dict and dict[i]!=0:
                dict[i] = 0
                total -= i 
            elif i in dict:
                pass
            else:
                dict[i] = 1
                total += i
        return total 

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.sumOfUnique([1,2,3,2]))