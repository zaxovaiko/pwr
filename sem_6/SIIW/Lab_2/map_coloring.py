import math
import time
import random as rd
from helpers import intersect
from gui import GUI
from csp import Constraint, CSP

LINE_DIS = 40

# For tests
F_WIDTH = 10
F_HEIGHT = 10
POINTS_NUMBER = int(input("Enter number of points: "))


def run_map_coloring():
    # Generates random points
    coords = []
    for _ in range(POINTS_NUMBER):
        point = [rd.randint(1, F_WIDTH), rd.randint(1, F_HEIGHT) ]
        if point not in coords:
            coords.append(point)
    coords = [ [ x * LINE_DIS, y * LINE_DIS ] for x, y in coords ]

    gui = GUI(F_WIDTH, F_HEIGHT)
    gui.draw_background()

    # Connect points randomly
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

    # Prepare data for csp
    # Does not belong to problem solving
    grouped = {str(c): [] for c in coords}
    for [s, ends] in lines:
        if str(s) in grouped: grouped[str(s)].append(ends)

    # Initiate constraints and variables for map coloring problem
    VAR = ['red', 'blue', 'green', 'black']
    CONSTRAINTS = []
    for x1 in grouped.keys():
        for x2 in grouped[x1]:
            CONSTRAINTS.append(Constraint([str(x1), str(x2)], lambda x, x1=x1, x2=x2: x[str(x1)][0] != x[str(x2)][0]))
    
    '''

    '''
    
    # Solve csp problem
    csp = CSP(list(VAR), { str(i): list(VAR) for i in grouped.keys() }, CONSTRAINTS)
    # csp.solve_backtracking()
    # csp.solve_forward_checking()
    csp.solve_ac3()
    
    if len(csp.sols) == 0:
        print('Solution does not exists')
        # gui.draw_color_points(coords, [x[0] for x in csp.doms.values()])
    else:
        # gui.draw_color_points(coords, [x[0] for x in csp.sols[0].values()])
        pass

    gui.root.mainloop()


if __name__ == '__main__':
    run_map_coloring()