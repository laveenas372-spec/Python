import collections

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        # Bitmasks for 4-seat blocks (Seats 2-9 mapped to bits 0-7)
        left = 0b00001111    # Seats 2, 3, 4, 5
        middle = 0b00111100  # Seats 4, 5, 6, 7
        right = 0b11110000   # Seats 6, 7, 8, 9
        
        occupied = collections.defaultdict(int)
        for row, col in reservedSeats:
            if 2 <= col <= 9:
                occupied[row] |= 1 << (col - 2)
        
        # Unreserved rows can fit 2 families each
        ans = (n - len(occupied)) * 2
        
        for bitmask in occupied.values():
            left_free = (bitmask & left) == 0
            right_free = (bitmask & right) == 0
            
            if left_free and right_free:
                ans += 2
            elif left_free or right_free or (bitmask & middle) == 0:
                ans += 1
                
        return ans