import time
from shapely.geometry import LineString

# Return true if line segments AB and CD intersect
def intersect(A, B, C, D):
    if A == C or A == D or B == C or B == D:
        return False
    return LineString([A, B]).intersects(LineString([C, D]))