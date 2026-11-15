# Sliding window approach
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""

        countT = {}
        for char in t:
            countT[char] = countT.get(char,0) + 1
        
        window = {}
        have = 0
        need = len(countT)
        res = [-1, -1]
        resLen = len(s) + 1
        l = 0

        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in countT and window[char] == countT[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # move left pointer to the right
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        return s[res[0]:res[1] + 1] if resLen != len(s) + 1 else ""

# Time: O(n + m) n is length of s, m is length of t
# Space: O(k) k is unique character in s and t


# # brute force
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         tCount = {}
#         for char in t:
#             tCount[char] = tCount.get(char, 0) + 1
        
#         l = 0
#         r = 0
#         shortest = len(s)
#         shortestStr = ""

#         while l < len(s):
#             have = 0
#             need = len(tCount)
#             window = {}
#             if tCount.get(s[l], 0):
#                 # print('left', l, 'right', r, shortest)
#                 # currCount = tCount.copy()
#                 # tSet = set(t)
#                 # expand window
#                 while r - l + 1 <= shortest and r < len(s):
#                     # print(s[l:r+1], l, r)
#                     window[s[r]] = window.get(s[r], 0) + 1
#                     if s[r] not in tCount:
#                         r+= 1
#                         continue;

#                     if window[s[r]] == tCount[s[r]]:
#                         have += 1
#                         if have == need:
#                             shortest = min(shortest, r - l + 1)
#                             shortestStr = s[l:r + 1]
#                         r += 1
#                     else:
#                         r += 1
#                     # print(window, tCount, have, need)
#                 l += 1
#                 r = l
#             else:
#                 l += 1
#                 r = l

#         return shortestStr
