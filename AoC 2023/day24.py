with open("AoC 2023\inputs\day24.txt", "r") as file:
    lines = [[[int(x) for x in triplet.split(", ")] for triplet in line.split(" @ ")] for line in file.read().split("\n")]

def hails_intersect(o1, d1, o2, d2):
    '''Checks if two rays intersect.
    First, check if O+Dt = O2+D2t for any t > 0, then check if within XY bounds
    We note that we are interested in whether the paths intersect, not if the actual hails collide (so t1 and t2 need not be the same)
    For part 1, only consider x and y, so only two equations:
    (1): o1x + d1x*t1 = o2x + d2x*t2
    (2): o1y + d1y*t1 = o2y + d2y*t2
    We solve Ax = b using inverse of A if det(A) exists
    '''
    det_A = d1[0]*d2[1] - d2[0]*d1[1]
    if abs(det_A) < 0.000001:
        # Rays are (almost) parallel
        return False

    dx = o2[0] - o1[0]
    dy = o2[1] - o1[1]
    rev_det = 1/det_A

    t1 = rev_det * ( d2[1]*dx - d2[0]*dy)
    t2 = rev_det * ( d1[1]*dx - d1[0]*dy)

    inter_x = o1[0] + d1[0]*t1
    inter_y = o1[1] + d1[1]*t1

    if t1 < 0 or t2 < 0:
        # Intersection is on the wrong side of the origin of the ray
        return False

    MIN_BOUND = 200000000000000
    MAX_BOUND = 400000000000000

    if  inter_x >= MIN_BOUND and inter_x <= MAX_BOUND and\
        inter_y >= MIN_BOUND and inter_y <= MAX_BOUND:
        # Intersect within the correct bounds
        return True
    else:
        # Intersect but not within the bounds
        return False

intersections = 0
for i, hail1 in enumerate(lines):
    for j, hail2 in enumerate(lines[i+1:]):
        ori1 = hail1[0]
        dir1 = hail1[1]

        ori2 = hail2[0]
        dir2 = hail2[1]

        if hails_intersect(ori1, dir1, ori2, dir2):
            intersections += 1


print("Part 1:", intersections)

# Part 2
'''We are solving an annoying but overdetermined system of equations
Looking for O = (x,y,z) and D = (u,v,w) such that the ray 
O+Dt intersects the rays from EACH hail at a matching t value.
O_rock+D_rock * t_i = O_hail_i + D_hail_i * t_i for all i hails

Each equation has an unknown t_i (intersection time), and we have 6 unknowns (3 for O, 3 for D)
With 3 hailstones we add 3 time points (a, b, c). We have 9 equations with 9 unknowns, thus solvable.
Unknowns: x, y, z, u, v, w, t1, t2, t3

We use first 3:
Hail 1: 320870677764563, 335750934489987, 282502845957937 @ -40, -24, 10
Hail 2: 219235623600942, 408022798608755, 245679379684914 @ 127, -45, 66
Hail 3: 171834827764229, 225154401936948, 232302441670972 @ -122, -521, 95

x + u*t1 = 320870677764563 - 40*t1
y + v*t1 = 335750934489987 - 24*t1
z + w*t1 = 282502845957937 + 10*t1

x + u*t2 = 219235623600942 + 127*t2
x + u*t3 = 171834827764229 - 122*t3
'''

import sympy
# Set variables
x, y, z, u, v, w, t1, t2, t3 = sympy.symbols('x, y, z, u, v, w, t1, t2, t3')

# Set 9 equations (3 dimensions per hail)
eq1 = sympy.Eq(x + u*t1, 320870677764563 -  40*t1)
eq2 = sympy.Eq(y + v*t1, 335750934489987 -  24*t1)
eq3 = sympy.Eq(z + w*t1, 282502845957937 +  10*t1)
eq4 = sympy.Eq(x + u*t2, 219235623600942 + 127*t2)
eq5 = sympy.Eq(y + v*t2, 408022798608755 -  45*t2)
eq6 = sympy.Eq(z + w*t2, 245679379684914 +  66*t2)
eq7 = sympy.Eq(x + u*t3, 171834827764229 - 122*t3)
eq8 = sympy.Eq(y + v*t3, 225154401936948 - 521*t3)
eq9 = sympy.Eq(z + w*t3, 232302441670972 +  95*t3)

# Solve system and output x+y+z
solved_vars = sympy.solvers.solve([eq1,eq2,eq3,eq4,eq5,eq6,eq7,eq8,eq9],dict=True)[0]
sum_of_pos = solved_vars[x] + solved_vars[y] + solved_vars[z]
print("Part 2:", sum_of_pos)
