from collections import namedtuple

"""
You can create data classes using namedtuple 
this has also magic method defined already. like (eq, gt, ls)etc
"""
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2, z=5)
p2 = Point(x=1, y=2)
print(p1)
