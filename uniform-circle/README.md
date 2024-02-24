# Generate Random Point in a Circle

## Problem Statement

So the problem requires you to write a function that generates random points which are evenly distributed inside a circle of given radius.

Let's say you are given a circle of radius R and the the center of the circle is (x_center, y_center). Your objective is to write a function `randPoint` which
returns [random_x, random_y] when invoked and is then used to generate N points inside the circle which are distributed evenly.

You can try solving and visualizing this in a programming language of your choice but I would recommend Python given the availability of Matplotlib library.
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

**Give this a try before heading over to the solution.**
