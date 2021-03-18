"""
--- Part Two ---
Amidst the chaos, you notice that exactly one claims doesn't overlap by even a single square inch of fabric with any other claims. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!

For example, in the claimss above, only claims 3 is intact after all claimss are made.

What is the ID of the only claims that doesn't overlap?
"""
from collections import defaultdict
import timeit


def listFromFile(filePath):
    file = open(filePath, 'r')
    res = []
    for line in file:
        res.append(ParseToClaim(line))
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
    # boxID @ x,y : 'width'x'height'
    boxID_and_rest = line.split('@')
    boxID = boxID_and_rest[0].strip()

    x_y_and_rest = boxID_and_rest[1].split(':')
    x_y = (x_y_and_rest[0].strip()).split(',')

    w_h = x_y_and_rest[1].strip().split('x')
    return Claim(boxID, int(x_y[0]), int(x_y[1]), int(w_h[0]), int(w_h[1]))


def isOverlap(claim1, claim2):
    width = max(claim1.x1, claim2.x1)-min(claim1.x2, claim2.x2)
    height = max(claim1.y1, claim2.y1)-min(claim1.y2, claim2.y2)
    return width > 0 and height > 0


def fillOverlapMap(overlap_map, inputData):
    for claim in inputData:
        for x in range(claim.x1, claim.x2):
            for y in range(claim.y1, claim.y2):
                overlap_map[(x, y)] = overlap_map.get((x, y), 0)+1


def isClaimInOverlapMap(claim, overlap_map):
    for x in range(claim.x1, claim.x2):
        for y in range(claim.y1, claim.y2):
            if overlap_map[(x,y)]>1:
                return True
    return False


def getIntactID(inputData):
    overlap_map = {}
    fillOverlapMap(overlap_map, inputData)

    print(len(overlap_map))
    for claim in inputData:
        if not isClaimInOverlapMap(claim, overlap_map):
            print(claim)
            break


print(timeit.timeit(str(getIntactID(listFromFile(
    '/home/legion/py-learning/adventofcode/_2018/3/input'))), number=1))
