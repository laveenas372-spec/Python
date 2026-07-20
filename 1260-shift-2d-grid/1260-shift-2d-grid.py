class Solution(object):
    def shiftGrid(self, grid, k):
       
       
        row = len(grid)
        col = len(grid[0])

        k %= (row * col)

        for _ in range(k):

            curr = grid[0][0]
            prev = grid[0][0]


            for r in range(row):
                for c in range(col):

                    prev = curr
                    curr = grid[r][c]
                    grid[r][c] = prev
            grid[0][0] = curr
        return grid