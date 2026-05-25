class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        map = {}

        index = 0

        while index < len(nums2):
            while stack and stack[-1] < nums2[index]:
                val = stack.pop(-1)
                map[val] = nums2[index]
            
            stack.append(nums2[index])
            index += 1

        for num in stack:
            map[num] = -1

        result = []

        for num in nums1:
            result.append(map[num])

        return result