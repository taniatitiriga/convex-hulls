import matplotlib.pyplot as plt

def orientation(p, q, r):
    """Return positive if p-q-r are clockwise, negative if counterclockwise, zero if collinear."""
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

def convex_hull(points):
    """Computes the convex hull of a set of 2D points."""
    points = sorted(points)  # sort points lexicographically (by x, then by y)

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

def points_on_hull(points, hull):
    """Returns the number of points from the original set that are on the convex hull."""
    return sum(1 for p in points if p in hull)

# the fixed points: from lab task
A = (3, -3)
B = (3, 3)
C = (-3, -3)
D = (-3, 3)

lambda_values = [-5, -1, -0.6, -0.3, 0, 5, 8]  # test values
results = []

for λ in lambda_values:
    M = (-2 + λ, 3 - λ)
    points = [A, B, C, D, M]
    
    # compute the convex hull
    hull = convex_hull(points)
    
    # count points on the convex hull
    count = points_on_hull(points, hull)
    results.append((λ, M, count))

    # ------visualization---------
    plt.figure(figsize=(6, 6))
    x, y = zip(*points)
    plt.scatter(x, y, label="Points")
    hx, hy = zip(*(hull + [hull[0]]))  # Close the hull
    plt.plot(hx, hy, 'r-', label="Convex Hull")
    plt.scatter(M[0], M[1], color='orange', label="M (λ={})".format(λ))
    plt.title(f"Convex Hull with λ={λ}")
    plt.legend()
    plt.grid(True)
    plt.show()

# results (number of points on the border)
for λ, M, count in results:
    print(f"λ = {λ}, M = {M}, Points on Convex Hull: {count}")
