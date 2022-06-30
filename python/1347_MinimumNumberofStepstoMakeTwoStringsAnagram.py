class Solution:
    def minSteps(self, s, t):
        '''

        dict1 = {"temp":0}
        dict1 = {}
        res = 0
        for i in list(s):
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        for i in list(t):
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
            
        if dict1 == dict1:
            return 0
      
        for key in dict1:
            try:
                dict1[key] -= dict1[key]

            except:
                dict1["temp"] -= dict1[key]
        for i in dict1.values():
            if i < 0:
                res -= i
        return res
        '''
        dict = {}
        res = 0
        if s == t:
            return res

        
        for (ch1, ch2) in zip(s , t):
            try:
                dict[ch1] += 1 
            except:
                dict[ch1] = 1
            try:
                dict[ch2] -= 1 
            except:
                dict[ch2] = -1

                        
        for v in dict.values():
            if v > 0:
                res += v
        
        return res
        
if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.minSteps("leetcode","practice"))