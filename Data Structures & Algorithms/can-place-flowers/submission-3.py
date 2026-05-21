class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0

        while i < len(flowerbed):
            if i == 0:
                # first index 
                if len(flowerbed) == 1 and flowerbed[i] == 0:
                    count += 1
                elif flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    count += 1
                    i += 1

            elif i == len(flowerbed) - 1:
                # last index
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    count += 1
            
            else:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    count += 1
                    i += 1

            i += 1

            print(f"index {i}: {count}")
        print(count)
        return count >= n