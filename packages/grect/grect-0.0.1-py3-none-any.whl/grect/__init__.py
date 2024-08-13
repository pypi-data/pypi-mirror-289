import math


def rotate_point(cx, cy, x, y, angle_radians):
    """Rotate a point counterclockwise around (cx, cy) by angle_radians."""
    x_rotated = cx + (x - cx) * math.cos(angle_radians) - (y - cy) * math.sin(angle_radians)
    y_rotated = cy + (x - cx) * math.sin(angle_radians) + (y - cy) * math.cos(angle_radians)
    return x_rotated, y_rotated


# Center of the rect
# Width and height of the rect
 # Angle of rotation in degrees
def generate_rectangle(center_x, center_y, width, height, angle_degrees):
    """Generate the coordinates of a rotated rect."""
    # Convert angle from degrees to radians  
    angle_radians = math.radians(angle_degrees)

    # Define the corners of the unrotated rect
    x0, y0 = center_x - width / 2, center_y - height / 2
    x1, y1 = center_x + width / 2, center_y - height / 2
    x2, y2 = center_x + width / 2, center_y + height / 2
    x3, y3 = center_x - width / 2, center_y + height / 2

    # Rotate the corners of the rect
    points = [
        rotate_point(center_x, center_y, x0, y0, angle_radians),
        rotate_point(center_x, center_y, x1, y1, angle_radians),
        rotate_point(center_x, center_y, x2, y2, angle_radians),
        rotate_point(center_x, center_y, x3, y3, angle_radians)
    ]

    return points
