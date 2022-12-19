# Batteries
import math

CM_IN_INCH = 2.54


def calc_height_width(height_px: int, width_px: int, diagonal_inch: float):
    diagonal_px = math.sqrt(height_px**2 + width_px**2)
    scale_inch = diagonal_inch / diagonal_px
    height_inch = height_px * scale_inch * CM_IN_INCH
    width_inch = width_px * scale_inch * CM_IN_INCH

    return height_inch, width_inch
