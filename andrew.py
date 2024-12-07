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
        return 0  # Collinear
    elif val > 0:
        return 1  # Clockwise
    else:
        return 2  # Counterclockwise

def andrews_algorithm(points):
    """
    Andrew's monotone chain algorithm to find the convex hull.
    This function builds both the lower and upper hulls.
    """
    points = sorted(points)  # Sort points lexicographically (x, then y)

    # Build the lower hull
    lower = []
    print("Building the lower hull:")
    for point in points:
        while len(lower) >= 2 and orientation(lower[-2], lower[-1], point) != 2:
            removed = lower.pop()
            print(f"Removing {removed} because it does not maintain counterclockwise orientation")
        lower.append(point)
        print(f"Added {point} to the lower hull: {lower}")

    # Build the upper hull
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and orientation(upper[-2], upper[-1], point) != 2:
            upper.pop()
        upper.append(point)

    # Remove the last point of each half because it's repeated at the beginning of the other half
    return lower[:-1] + upper[:-1]

# Input points
points = [(1, 10), (-2, 7), (3, 8), (4, 10), (5, 7), (6, 7), (7, 11)]

# Compute the convex hull
hull = andrews_algorithm(points)

# Visualization
plt.figure(figsize=(8, 8))
x, y = zip(*points)
plt.scatter(x, y, label="Points", zorder=5)

# Draw the convex hull
hx, hy = zip(*(hull + [hull[0]]))  # Close the hull by adding the first point at the end
plt.plot(hx, hy, 'r-', label="Convex Hull", zorder=10)

# Annotate points for clarity
for i, (px, py) in enumerate(points):
    plt.text(px + 0.2, py, f"P{i+1}", fontsize=9)

plt.title("Convex Hull (Andrew's Algorithm)")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()
