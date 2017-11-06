def cross_product(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return x1 * y2 - x2 * y1

def origin_in_interior(triangle):
    p1, p2, p3 = triangle
    point_pairs = [(p1, p2), (p2, p3), (p3, p1)]
    sin_angles = [cross_product((xb - xa, -xa), (yb - ya, -ya))
        for (xa, ya), (xb, yb) in point_pairs]
    return all([a > 0 for a in sin_angles]) or all([a < 0 for a in sin_angles])

def parse_line(line):
    coords = [int(i) for i in line.split(',')]
    return ((coords[0], coords[1]), (coords[2], coords[3]), (coords[4], coords[5]))

def main():
    with open('resources/p102_triangles.txt', 'r') as f:
        triangles = (parse_line(line) for line in f)
        print sum(1 for t in triangles if origin_in_interior(t))

if __name__ == '__main__':
    main()
