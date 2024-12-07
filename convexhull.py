import matplotlib.pyplot as plt

# -------Graham's Scan-------
def orientation(p, q, r):
    """Return positive if p-q-r are clockwise, negative if counterclockwise, zero if collinear."""
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

def convex_hull(points):
    """Computes the convex hull."""
    points = sorted(points)

    # lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

# example: from lab task
points = [(30, 60), (15, 25), (0, 30), (70, 30), (50, 40), (50, 10), (20, 0), (55, 20)]

# compute convex hull
hull = convex_hull(points)

# ------visualization---------
plt.figure(figsize=(8, 8))
x, y = zip(*points)
plt.scatter(x, y, label="Points", zorder=5)

hx, hy = zip(*(hull + [hull[0]]))
plt.plot(hx, hy, 'r-', label="Convex Hull", zorder=10)

for i, (px, py) in enumerate(points):
    plt.text(px + 1, py, f"P{i+1}", fontsize=9)

plt.title("Convex Hull Visualization")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()
