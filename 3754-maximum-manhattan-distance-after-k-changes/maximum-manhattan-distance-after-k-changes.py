class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        directions = {
            'north' : 0,
            'south' : 0,
            'east' : 0,
            'west' : 0
        }

        for i in range(n):
            d = s[i]
            if d == 'N':
                directions['north'] += 1
            elif d == 'S':
                directions['south'] += 1
            elif d == 'E':
                directions['east'] += 1
            elif d == 'W':
                directions['west'] += 1

            x = abs(directions['north'] - directions['south'])
            y = abs(directions['east'] - directions['west'])
            md = x + y
            dist = md + min(2*k, i+1-md)
            res = max(res, dist)

        return res