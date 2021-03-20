"""--- Day 6: Chronal Coordinates ---
The device on your wrist beeps several times, and once again you feel like you're falling.

"Situation critical," the device announces. "Destination indeterminate. Chronal interference detected. Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they places it thinks are safe or dangerous? It recommends you check manual page 729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the coordinate that gives the largest distance from the other points.

Using only the Manhattan distance, determine the area around each coordinate by counting the number of integer X,Y locations that are closest to that coordinate (and aren't tied in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite. For example, consider the following list of coordinates:

1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
If we name these coordinates A through F, we can draw them on a grid, putting 0,0 at the top left:

..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.
This view is partial - the actual grid extends infinitely in all directions. Using the Manhattan distance, each location's closest coordinate can be determined, shown here in lowercase:

aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf
Locations shown as . are equally far from two or more coordinates, and so they don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their areas extend forever outside the visible grid. However, the areas of coordinates D and E are finite: D is closest to 9 locations, and E is closest to 17 (both including the coordinate's location itself). Therefore, in this example, the size of the largest area is 17.

What is the size of the largest area that isn't infinite?"""

import collections

PATH = '_2018/day6/input'


def getData():
    with open(PATH) as f:
        temp = f.read().splitlines()
        data = [tuple([int(val) for val in point.split(',')])
                for point in temp]
        return data


def buildGrid(points, grid):
    max_x = 0
    max_y = 0
    min_x = -1
    min_y = -1

    for point in points:
        if min_y < 0 or min_x < 0:
            min_x = point[0]
            min_y = point[1]
        max_x = max(max_x, point[0])
        max_y = max(max_y, point[1])
        min_x = min(min_x, point[0])
        min_y = min(min_y, point[1])

    res = (max_x+1, max_y+1, min_x-1, min_y-1)

    for x in range(res[2], res[0]):
        for y in range(res[3], res[1]):
            grid.append((x, y))

    return res


def isInfiniteCoordinate(owner_point, infinite_coordinates):
    return (owner_point[0] == infinite_coordinates[0]
            or owner_point[0] == infinite_coordinates[2]
            or owner_point[1] == infinite_coordinates[1]
            or owner_point[1] == infinite_coordinates[3])


def getArea(points):
    # {Tuple(grid point coordinates): Tuple(owner_point coordinates)}
    grid = []
    area_counter = collections.Counter()
    infinite_area_owners = []

    infinite_coordinates = buildGrid(points, grid)
    for grid_coordinates in grid:
        distances = collections.defaultdict(list)

        for owner_candidate in points:
            distance = (abs(owner_candidate[0]-grid_coordinates[0]) +
                        abs(owner_candidate[1]-grid_coordinates[1]))
            distances[distance].append(owner_candidate)

        sorted_distances = sorted(distances.keys(), reverse=True)

        if len(distances[sorted_distances[-1]]) < 2:
            owner_point = distances[sorted_distances[-1]][0]

            if isInfiniteCoordinate(grid_coordinates, infinite_coordinates):
                infinite_area_owners.append(owner_point)

                if owner_point in area_counter:
                    del area_counter[owner_point]
                    continue

            if owner_point not in infinite_area_owners:
                area_counter[owner_point] += 1

    print('most_common:', area_counter.most_common(1))

    #print(max_x, max_y, min_x, min_y)


getArea(getData())
