''' it should be right but leetcode said it is wrong
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for i in list(t):
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        for i in list(s):
            if  i in map and i!=0:
                map[i] -=1
            else:
                return False
        for i in map.values():
            if i >0:
                return False
 
        return True
                
        
'''
class Solution:

    def isAnagram(self,s,t):
        map1 = {}
        map2 = {}
        for i in list(s):
            if i in map1:
                map1[i] += 1
            else:
                map1[i] = 1

        for i in list(t):
            if i in map2:
                map2[i] += 1
            else:
                map2[i] = 1
        if map1 == map2:
            return True

        return False

        
        
                
        
if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.isAnagram("aaa","aaa"))
