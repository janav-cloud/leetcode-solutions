class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # Sort intervals by start time
        k = 0 # Index for merged intervals
        
        for i in range(1, len(intervals)):
            if intervals[k][1] >= intervals[i][0]: # Overlap detected
                intervals[k][1] = max(intervals[k][1], intervals[i][1]) # Merge
            else:
                k += 1 # Move to the next position
                intervals[k] = intervals[i] # Replace in-place
        
        return intervals[:k + 1] # Return only merged intervals