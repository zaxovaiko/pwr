import tkinter as tk

LINE_DIS = 40
POINT_RADIUS = 5

class GUI:
    def __init__(self, f_width, f_height):
        self.f_width = f_width
        self.f_height = f_height

        self.root = tk.Tk()
        self.root.title('cspoblem kolorowania mapy')
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
            self.draw_circle(*point, color=color)

    def draw_points(self, coords):
        for co in coords:
            self.draw_circle(*co)