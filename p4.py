from aoc_utils import DIRECTIONS8

FNAME = "in4.txt"
    
# load the map
grid = [list(line) for line in open(FNAME).read().splitlines()]
height = len(grid)
width = len(grid[0])

# check if we have a legal x, y
def inbounds(x, y):
    return 0 <= x < width and 0 <= y < height

# find a list of all points adjacent to the (x, y) that contain rolls
def neighbor_rolls(x, y):
    points = []
    for dx, dy in DIRECTIONS8:
        if inbounds(x + dx, y + dy) and grid[y + dy][x + dx] == "@":
            points.append((x + dx, y + dy))
    return points
        
# find a list of all points that contain rolls w/ < 4 adjacent rolls
points = []
for x in range(width):
    for y in range(height):
        if grid[y][x] == "@" and len(neighbor_rolls(x, y)) < 4:
            points.append((x, y))
           
part1 = len(points)
print("Part 1:", part1) # 1491

# now do this over and over again until no more rolls are accessible
part2 = part1

# as long as there are accessible points...
while points:
    
    # remove the rolls in those points
    for x, y in points:
        grid[y][x] = '.'
        
    # then look for new accessible points
    points = []
    for x in range(width):
        for y in range(height):
            if grid[y][x] == "@" and len(neighbor_rolls(x, y)) < 4:
                points.append((x, y))
               
    part2 += len(points)
                
print("Part 2:", part2) # 8722
