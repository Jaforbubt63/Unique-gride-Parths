import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        
        m -= 1
        n -= 1
        path_count = math.factorial(m+n) / (math.factorial(m) * math.factorial(n))
        
        
        
        return int(path_count)
 