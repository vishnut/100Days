def getBiggestRegion(grid):
    num = 2
    for i, ix in enumerate(grid):
        for j, _ in enumerate(ix):
            if grid[i][j] == 1:
                convertRegion(grid, i, j, num)
                num += 1
    vals = {}
    for i in grid:
        for j in i:
            if j > 1:
                if j in vals:
                    vals[j] += 1
                else:
                    vals[j] = 1
    maxval = 0
    for _, v in vals.items():
        if v > maxval:
            maxval = v
    return maxval

def convertRegion(grid, i, j, num):
    if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[i]):
        if grid[i][j] == 1:
            grid[i][j] = num
            convertRegion(grid, i - 1, j, num)
            convertRegion(grid, i - 1, j + 1, num)
            convertRegion(grid, i - 1, j - 1, num)
            convertRegion(grid, i + 1, j, num)
            convertRegion(grid, i + 1, j + 1, num)
            convertRegion(grid, i + 1, j - 1, num)
            convertRegion(grid, i, j + 1, num)
            convertRegion(grid, i, j - 1, num)
    
n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))
