# Stack approach
class Solution:
    def isValid(self, s: str) -> bool:
        pairMap = {'(': ')', '{': '}', '[': ']'}
        openSet = set(pairMap.keys())
        closeSet = set(pairMap.values())

        stack = []

        for char in s:
            if char in openSet:
                stack.append(char)
            elif char in closeSet:
                if not len(stack): return False

                closeChar = pairMap[stack.pop()]
                if closeChar != char:
                    return False
            else:
                return False
        
        return len(stack) == 0

# Time: O(n) for iterating s
# Space: O(n)
