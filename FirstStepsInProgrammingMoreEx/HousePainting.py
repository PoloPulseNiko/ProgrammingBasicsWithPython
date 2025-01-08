x = float(input())
y = float(input())
h = float(input())


front_back = 2 * (x * x) - (1.2 * 2)
side_walls = 2 * (x * y) - 2 * (1.5 * 1.5)
roof_rectangles = 2 * (x * y)
roof_triangles = 2 * ((x * h) / 2)

green_paint_area = front_back + side_walls
red_paint_area = roof_rectangles + roof_triangles

green_paint_needed = green_paint_area / 3.4
red_paint_needed = red_paint_area / 4.3

print(f"{green_paint_needed:.2f}")
print(f"{red_paint_needed:.2f}")
