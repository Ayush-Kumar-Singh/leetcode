class Solution:
    def romanToInt(self, s: str) -> int:
        g = 0
        array = ["IV","IX","XL","XC","CD","CM"]
        for x in array:
            if(x in s):
                s =s.replace(x,"")
                if("IV" in x):
                    g = g+4
                elif( "IX" in x):
                    g = g+9
                elif("XL" in x):
                    g = g+40
                elif("XC" in x):
                    g = g+90
                elif("CD" in x):
                    g = g+400
                elif(x == "CM" in x):
                    g = g+900
            
        
        
        ayush =[d for d in str(s)]
        
        for x in ayush:
            if(x == "I"):
                g= g +1
            elif(x == "V"):
                g = g+5
            elif(x == "X"):
                g = g +10
            elif(x == "L"):
                g = g + 50
            elif(x == "C"):
                g = g + 100
            elif(x == "D"):
                g = g + 500
            elif(x == "M"):
                g = g + 1000
        return g
        
