from display import *
from draw import *
from parser import *
from matrix import *
import math


# lighting values
view = [0,
        0,
        1];
ambient = [50,
           50,
           50]
light = [[0.5,
          0.75,
          1],
         [0,
          255,
          255]]
areflect = [0.1,
            0.1,
            0.1]
dreflect = [0.5,
            0.5,
            0.5]
sreflect = [0.5,
            0.5,
            0.5]



screen = new_screen()
zbuffer = new_zbuffer()
color = [ 0, 255, 0 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]


#parse_file( 'script', edges, polygons, csystems, screen, zbuffer, color, view, ambient, light, areflect, dreflect, sreflect)


screen2 = new_screen()
t2 = new_matrix()
ident(t2)
csystems2 = [ t2 ]
bowl = []
cx = 250
cy = 150
cz = 0
r = 5
height = 0
while height<=150:
    add_torus(bowl, cx, cy+height, cz, 5, r, 20)
    r+=5
    height=int((r**4)/9000000.0)
fruit = []
add_sphere(fruit, 250, 205, 0, 50, 20)
add_box(bowl, 245, -100, -5, 10, 250, 10)
# parse_file('script2', edges, fruit, csystems2, screen2, zbuffer, color, view, ambient, light, areflect, dreflect, sreflect)
# parse_file('script2', edges, bowl, csystems2, screen2, zbuffer, color, view, ambient, light, areflect, dreflect, sreflect)
save_extension(screen2, 'bowl.png')
