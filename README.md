# Convex Hulls and Polygon Algorithms
This repository contains Python implementations of several computational geometry algorithms, focusing on convex hulls, polygons, and related tasks. The algorithms include Andrew's Monotone Chain, Jarvis March, and more, with step-by-step visualization and explanations.

## Repository structure
This repository contains the following Python scripts:
1. `convexhull.py`:
  - Computes the convex hull of a given set of points using **Graham's Scan algorithm**.
  - Visualizes the result with `matplotlib`
2.  `lambda_convexhull.py`:
  - Computes and visualizes how the **convex hull changes with a dynamic point** \( M = (-2 + \lambda, 3 - \lambda) \), where \( \lambda \in \mathbb{R} \).
  - Focuses on visualizing step-by-step how 𝑀 influences the convex hull, printing in the console the number of points on the border for each value of \( \lambda \).
3.  `polygon.py`:
  - Computes the valid **polygon that contains a given set of points as vertices**.
  - Visualizes the result with `matplotlib`
4.  `jarvismarch.py`:
  - Implements **the Jarvis March algorithm** to compute the convex hull.
  - Focuses on the selection process of successors using the orientation test. Contains detailed descriptions of that process within the functions code.
5.  `andrew.py`:
  - Implements **Andrew's Monotone Chain Algorithm** to compute the convex hull.
  - Prints detailed logs for the step-by-step construction of the **lower hull**.

