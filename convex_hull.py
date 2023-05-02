import rhinoscriptsyntax as rs

def orientation(p, q, r):
    #Return positive value if p-q-r are clockwise, negative if counterclockwise, and 0 if colinear."""
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return -1

def convex_hull(points):
    #Return a list of points representing the convex hull of a set of points.
    n = len(points)
    if n < 3:
        return points
    hull = []
    l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i
    p = l
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == -1:
                q = i
        p = q
        if p == l:
            break
    return hull

# Compute the convex hull points
hull_points = convex_hull([rs.PointCoordinates(pt) for pt in rs.GetObjects("Points!!", 1, preselect=True)])

# Add the hull polyline to the document
hull_polyline = rs.AddPolyline(hull_points + [hull_points[0]])
