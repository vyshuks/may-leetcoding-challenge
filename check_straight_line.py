"""
You are given an array coordinates, coordinates[i] = [x, y],
where [x, y] represents the coordinate of a point. Check if
these points make a straight line in the XY plane.
"""


def check_straight_line(coordinates):
    """
    check given coordinates
    are in a straight line
    :param coordinates: List
    :return: bool
    """
    l = len(coordinates)
    if l == 2:
        return True
    x0,y0 = coordinates[0]
    x1,y1 = coordinates[1]
    for coordinate in range(2, l):
        x,y = coordinate
        if (y1-y0) * (x-x0) != (x1-x0) * (y-y0):
            return False
    return True

