import matplotlib.pyplot as plt
import math

def calculate_centroid(points):
    """Calculate the centroid of a set of points."""
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    return (sum(x_coords) / len(points), sum(y_coords) / len(points))

def polar_angle(point, centroid):
    """Calculate the polar angle of a point relative to the centroid."""
    x, y = point
    cx, cy = centroid
    return math.atan2(y - cy, x - cx)

def sort_points_by_angle(points):
    """Sort points by their polar angle relative to the centroid."""
    centroid = calculate_centroid(points)
    return sorted(points, key=lambda p: polar_angle(p, centroid))

# input points
points = [(4, 2), (7, -1), (3, -5), (-3, 6), (-4, 4), (-1, -1), (-2, -6)]

# sort the points (to avoid sides of the polygon intersecting)
sorted_points = sort_points_by_angle(points)

# close the polygon (appending the first point)
polygon_points = sorted_points + [sorted_points[0]]

# ------visualization---------
plt.figure(figsize=(8, 8))
x, y = zip(*points)
plt.scatter(x, y, label="Points", zorder=5)

px, py = zip(*polygon_points)
plt.plot(px, py, 'r-', label="Polygon", zorder=10)

for i, (px, py) in enumerate(points):
    plt.text(px + 0.3, py, f"P{i+1}", fontsize=9)

plt.title("Polygon with all points as vertices")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()
