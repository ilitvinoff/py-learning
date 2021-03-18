"""
--- Day 3: No Matter How You Slice It ---
The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still affecting them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:

The number of inches between the left edge of the fabric and the left edge of the rectangle.
The number of inches between the top edge of the fabric and the top edge of the rectangle.
The width of the rectangle in inches.
The height of the rectangle in inches.
# 123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:
A claim like

...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........
The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:

# 1 @ 1,3: 4x4
# 2 @ 3,1: 4x4
# 3 @ 5,5: 2x2
Visually, these claim the following areas:

........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)

If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric are within two or more claims?
"""
import timeit

def listFromFile(filePath):
    file = open(filePath, 'r')
    res = file.read().splitlines()
    return res


class Claim:
    def __init__(self, id, x, y, width, height) -> None:
        self.id = id
        self.x1 = x
        self.y1 = y
        self.x2 = x+width
        self.y2 = y+height

    def __str__(self) -> str:
        return 'id:{}; x1:{}; y1:{}; x2:{}; y2:{};'.format(self.id, self.x1, self.y1, self.x2, self.y2)


def ParseToClaim(line):
    #boxID @ x,y : 'width'x'height'
    boxID_and_rest = line.split('@')
    boxID = boxID_and_rest[0].strip()

    x_y_and_rest = boxID_and_rest[1].split(':')
    x_y = (x_y_and_rest[0].strip()).split(',')

    w_h = x_y_and_rest[1].strip().split('x')
    return Claim(boxID, int(x_y[0]), int(x_y[1]), int(w_h[0]), int(w_h[1]))


def getTotalOverlap(inputData):
    res = 0
    overlap_map = {}
    for line in inputData:
        claim = ParseToClaim(line)
        for x in range(claim.x1, claim.x2):
            for y in range(claim.y1, claim.y2):
                overlap_map[(x, y)] = overlap_map.get((x, y), 0)+1
                if overlap_map[(x, y)] == 2:
                    res += 1

    print(res)

print(timeit.timeit(str(getTotalOverlap(listFromFile('_2018/3/input'))),number=1))
