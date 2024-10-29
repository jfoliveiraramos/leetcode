from typing import List

class Solution:

    def exploreNext(self, grid: List[List[int]], row: int, col: int):

        max_moves = 0
        if col + 1 < len(grid[0]):

            curr = grid[row][col]

            if grid[row][col + 1] > 0 and grid[row][col + 1] > curr:
                max_moves = max(max_moves, self.exploreNext(grid, row, col + 1) + 1)
                grid[row][col + 1] = 0

            if row - 1 >= 0 and grid[row - 1][col + 1] > 0 and grid[row - 1][col + 1] > curr:
                max_moves = max(max_moves, self.exploreNext(grid, row - 1, col + 1) + 1)
                grid[row - 1][col + 1] = 0

            if row + 1 < len(grid) and grid[row + 1][col + 1] > 0 and grid[row + 1][col + 1] > curr:
                max_moves = max(max_moves, self.exploreNext(grid, row + 1, col + 1) + 1)
                grid[row + 1][col + 1] = 0
        
        return max_moves

    def maxMoves(self, grid: List[List[int]]) -> int:
     
        max_moves = 0

        for row in range(len(grid)):
            max_moves = max(max_moves, self.exploreNext(grid, row, 0))

        return max_moves
