import matplotlib.pyplot as plt

def orientation(p, q, r):
    """
    Return:
    0 -> p, q, and r are collinear
    1 -> Clockwise
    2 -> Counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # collinear
    elif val > 0:
        return 1  # clockwise
    else:
        return 2  # counterclockwise

def jarvis_march(points):
    """
    Jarvis March algorithm to find the convex hull.
    1. The successor of the leftmost point is found through the orientation() function.
    The successor is the most counterclockwise point relative to the current point.
    2. The process is repeated identically with the successor of the leftmost point, as well as with the lowest point.
    The tests remain unchanged, as the successor's "counterclockwise" property is relative to the current point.
    """
    n = len(points)
    if n < 3:
        return points
    
    # starting with the lowest point
    start = min(points, key=lambda p: (p[1], p[0]))
    hull = [] 

    current = start
    while True:
        hull.append(current)
        
        # start with the first point as a candidate
        next_point = points[0]
        
        for candidate in points:
            # find the most counterclockwise point relative to the current point
            if (next_point == current or
                orientation(current, next_point, candidate) == 2):
                next_point = candidate
        
        current = next_point
        if current == start:
            break
    
    return hull

# example points
points = [(2, -1), (1, 3), (4, 0), (4, 3), (5, 2)]

hull = jarvis_march(points)

# ------visualization---------
plt.figure(figsize=(8, 8))
x, y = zip(*points)
plt.scatter(x, y, label="Points", zorder=5)

hx, hy = zip(*(hull + [hull[0]]))
plt.plot(hx, hy, 'r-', label="Convex Hull", zorder=10)

for i, (px, py) in enumerate(points):
    plt.text(px + 0.2, py, f"P{i+1}", fontsize=9)

plt.title("Jarvis March Convex Hull")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()
