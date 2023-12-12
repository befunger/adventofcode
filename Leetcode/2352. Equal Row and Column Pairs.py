class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Create a dict with count of each column sequence
        # Go through each row, and if it matches a dict entry, increment output with the count

        # Add all columns to dict (with value indicating number of same columns)
        columns = {}
        for i,_ in enumerate(grid):
            # Convert list into space-separated string
            col = " ".join(str(row[i]) for row in grid)
            if col in columns:
                columns[col] += 1
            else:
                columns[col] = 1

        # Find number of matches for each row and add them up
        matches = 0
        for i,grid_row in enumerate(grid):
            row = " ".join(str(x) for x in grid_row)
            if row in columns:
                matches += columns[row]

        return matches
