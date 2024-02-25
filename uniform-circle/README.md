# Generate Random Points in a Circle

## Problem Statement

So the problem requires you to write a function that generates random points that are evenly distributed inside a circle of a given radius.

Let's say you are given a circle of radius R and the the center of the circle is (x_center, y_center). Your objective is to write a function `randPoint` which
returns [random_x, random_y] when invoked and is then used to generate N points inside the circle which are distributed evenly.

You can try solving and visualizing this in a programming language of your choice but I would recommend Python given the availability of the Matplotlib library.
If you are using Python you can use this template if you want to use my program to visualize your solution.

Just edit the `randPoint` function with your logic to generate the coordinates. The `plot` function is already written for you.

```python
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> list[float]:
        x = "Expression to generate x coordinate"
        y = "Expression to generate y coordinate"
        return [x, y]

    def plot(self, description):
      # Calls randPoint func and plots your solution
      pass
```

You can use the following code to instantiate this class and generate the plot:

```python
radius = 5
s = Solution(radius, 0, 0)
s.plot("• Plot description")
```

After you are done writing the logic you can run the script. Before running make sure you install the dependencies.

```bash
pip3 install numpy matplotlib
python3 circle.py
```

References:

1. [math - Generate a random point within a circle (uniformly) - Stack Overflow](https://stackoverflow.com/questions/5837572/generate-a-random-point-within-a-circle-uniformly)
2. [Uniform random points in a circle using polar coordinates – anderswallin.net](https://www.anderswallin.net/2009/05/uniform-random-points-in-a-circle-using-polar-coordinates/)
3. [3d - Uniform random (Monte-Carlo) distribution on unit sphere - Stack Overflow](https://stackoverflow.com/questions/1841014/uniform-random-monte-carlo-distribution-on-unit-sphere)
4. [Sphere Point Picking -- from Wolfram MathWorld](https://mathworld.wolfram.com/SpherePointPicking.html)
5. [Finding all the points within a circle in 2D space – iTecNote](https://itecnote.com/tecnote/r-finding-all-the-points-within-a-circle-in-2d-space/)
6. [What is Rejection Sampling? | Kapil Sachdeva | Towards Data Science](https://towardsdatascience.com/what-is-rejection-sampling-1f6aff92330d)
7. [6.3 Rejection Sampling | Advanced Statistical Computing](https://bookdown.org/rdpeng/advstatcomp/rejection-sampling.html)
