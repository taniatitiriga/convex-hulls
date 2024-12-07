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

## Prerequisites
Ensure you have the following installed:
- Python 3.7 or later
- pip (Python package manager)

You can check your Python version using:
```
python --version
```

## Installation
1. Clone the Repository:
```
git clone https://github.com/taniatitiriga/convex-hulls.git
cd convex-hulls
```
2. Set Up a Virtual Environment (Optional but Recommended):
```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```
3. Install Required Libraries: Install `matplotlib` for visualization:
```
pip install matplotlib
```

## Usage
Each script can be executed individually to see its functionality. Below are the details for each:
1. `convexhull.py`
  - **Task:** Implement one of the algorithms presented in the last lecture to obtain the same result.
  - **Run the script** (or you can use your prefered IDE - I use VSCode):
```
python convexhull.py
```
2. `lambda_convexhull.py`
  - **Task:** Implement an algorithm that will indicate the number of points on the border of the convex hull of the set.
  - **Run the script** (or you can use your prefered IDE - I use VSCode):
```
python lambda_convexhull.py
```
3. `polygon.py`
  - **Task:** Given n points in the plane, write an algorithm with complexity O(n log n) to determine a polygon that has all these points as vertices.
  - **Run the script** (or you can use your prefered IDE - I use VSCode):
```
python polygon.py
```
4. `jarvismarch.py`
  - **Task:** Specify the tests to be performed, when Jarvis March algorithm is applied, for determining the successor M of the "leftmost" point and of M's successor.
  - **Run the script** (or you can use your prefered IDE - I use VSCode):
```
python jarvismarch.py
```
1. `andrew.py`
  - **Task:** Detail how the evolution of the vertices during the determination of the lower edge of the border of the convex hull for M is obtained during Andrew's variant of Graham's scan.
  - **Run the script** (or you can use your prefered IDE - I use VSCode):
```
python andrew.py
```
