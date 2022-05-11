class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pico=[]
        ak = nums
        for x in nums:
            y = target - x
            yashu = nums.index(x)
            print(x)
            
            if(y ==y):
                if(y in nums):
                    ayush = nums.index(y)
                    if(ayush!=yashu):
                        pico.append(yashu)
                        pico.append(ayush)
                        break
                    elif(x==y and ayush == yashu):
                        if(nums.count(y) > 1):
                            
                            if(y in ak):
                                for x in range(len(nums)):
                                    if nums[x] == y and x != ayush:
                                        pico.append(yashu)
                                        pico.append(x)
                                break
        return pico              
                    
