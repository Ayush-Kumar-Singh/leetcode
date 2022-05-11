class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x>=0):
            ayush = [int(d) for d in str(x)]
            w = len(ayush)
            num=[]
            while(w>0):
                w = w-1
                num.append(ayush[w])
            res = int("".join(map(str, num)))
            if(res == x):
                return True
            else:
                return False
