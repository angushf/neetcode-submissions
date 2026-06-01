class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        myMap = {}
        counter = 0

        for i in range(len(text)):
            l = text[i]

            if l == "b" or l == "a" or l =="l" or l == "o" or l == "n":
                myMap[l] = myMap.get(l, 0) + 1

        if len(myMap) != 5:
            return counter

        while True:
            for key, val in myMap.items():
                if key == "l" or key == "o":
                    if val < 2:
                        return counter
                    
                    myMap[key] = myMap[key] - 2
                else: 
                    if val < 1:
                        return counter
                        
                    myMap[key] = myMap[key] - 1

            counter += 1
            

