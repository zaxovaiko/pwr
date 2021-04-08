
import math
import numpy as np
import random as rd
import tkinter as tk
from shapely.geometry import LineString


FILENAME = 'test0.txt'
LINE_DIS = 40
POINT_RADIUS = 5
COLORS = ['red', 'blue', 'green']

# For tests
F_WIDTH = 10
F_HEIGHT = 10
POINTS_NUMBER = 4

# rd.seed(200)


# Return true if line segments AB and CD intersect
def intersect(A, B, C, D):
    if A == C or A == D or B == C or B == D:
        return False
    return LineString([A, B]).intersects(LineString([C, D]))


def read_file(filename):
    with open('./data/' + filename, 'r') as f:
        # Return array with points, max width and height of the field
        coords = [ list(map(int, x.split(';'))) for x in f.readlines() ]
        return coords, np.max(np.array(coords)[:,0]), np.max(np.array(coords)[:,1])


# coords, F_WIDTH, F_HEIGHT = read_file(FILENAME)

coords = [ [rd.randint(1, F_WIDTH), rd.randint(1, F_HEIGHT) ] for _ in range(POINTS_NUMBER) ]
coords = [ [ x * LINE_DIS, y * LINE_DIS ] for x, y in coords ]

print(coords)


class GUI:
    def __init__(self, f_width, f_height):
        self.f_width = f_width
        self.f_height = f_height

        self.root = tk.Tk()
        self.root.title('Problem kolorowania mapy')
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=(1 + f_width) * LINE_DIS, height=(1 + f_height) * LINE_DIS, bg="#fff")
        self.canvas.pack()
        self.root.update()

    def draw_circle(self, x, y, radius=POINT_RADIUS, color='#000'):
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline='')

    def draw_background(self):
        for i in range(1, self.f_height + 1):
            for j in range(1, self.f_width + 1):
                self.draw_circle(i * LINE_DIS, j * LINE_DIS, color='#eee')

    def draw_line(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2, fill="#242424")

    def draw_color_points(self, coords, colors):
        for point, color in zip(coords, colors):
            self.draw_circle(*point, color=COLORS[color - 1])

    def draw_points(self, coords):
        for co in coords:
            self.draw_circle(*co)


gui = GUI(F_WIDTH, F_HEIGHT)
gui.draw_background()


lines = []

for _ in range(3):
    rd.shuffle(coords)
    for X in coords:
        # Sort by euclidean distance and get the first nearest
        dstn = sorted(coords, key=lambda point: math.dist(point, X))

        for Y in dstn[1:]:
            # If two points on the line have been already chosen
            if [X, Y] in lines or [Y, X] in lines: continue
            
            # Check if current line intersects any other
            if any(map(lambda x: intersect(X, Y, *x), lines)): continue

            gui.draw_line(*X, *Y)
            lines.append([X, Y])
            break

lines


solutions = []

# Make graph from coords
color = [0] * len(coords)
graph = [ [0] * len(coords) for _ in range(len(coords)) ]
for s, e in lines:
    r = coords.index(s)
    c = coords.index(e)
    graph[r][c] = 1


def bt(graph, m, color):
    if rbt(graph, m, color, 0) == None:
        return False
    return True


def rbt(graph, m, color, v) -> bool:
    if v == len(coords):
        return True

    for col in range(1, m + 1):
        if is_complete(graph, v, color, col): 
            color[v] = col
            if rbt(graph, m, color, col + 1):
                return True
            color[v] = 0


def is_complete(graph, v, color, c) -> bool:
    return not any( graph[v][i] and color[i] == c for i in range(len(graph)) )


res = bt(graph, len(COLORS), color)
print('Solution does not exists' if not res else color)


"""
### CSP - map-coloring problem

- Variables - points (regions)
- Domains - colors (red, blue, green, etc)
- Contraints - adjacent regions must have different colors
"""


gui.draw_color_points(coords, color)
# gui.draw_points(coords)
gui.root.mainloop()