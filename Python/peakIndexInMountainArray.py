#https://leetcode.com/problems/peak-index-in-a-mountain-array/

def peakIndexInMountainArray(self, A: List[int]) -> int:
    if len(A) < 3 or len(A) > 10000:
        return 0
    peak = None
    for i, val in enumerate(A):
        if i == 0:
            continue
        if val > A[i-1]:
            if i == len(A) - 1:
                return 0
            if val > A[i + 1]:
                if not peak:
                    peak = i
                else:
                    return 0
    return peak
