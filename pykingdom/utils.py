import pykingdom.gradients
from pygame import Surface, PixelArray

def rshift(val, n): return (val % 0x100000000) >> n

def interpolate_color(color1, color2, f):
    a1 = rshift(color1, 24)
    r1 = color1 >> 16 & 0xFF
    g1 = color1 >> 8 & 0xFF
    b1 = color1 & 0xFF

    a2 = rshift(color2, 24)
    r2 = color2 >> 16 & 0xFF
    g2 = color2 >> 8 & 0xFF
    b2 = color2 & 0xFF

    fi = 1 - f

    a1 = (fi * a1) + (f * a2)
    r1 = (fi * r1) + (f * r2)
    g1 = (fi * g1) + (f * g2)
    b1 = (fi * b1) + (f * b2)

    return a1 << 24 | r1 << 16 | g1 << 8 | b1

def gradient_overlay(bitmap, colors):
    colors_iterable = []
    for color in colors:
        r = int(((color >> 32) & 0xFF))
        g = int(((color >> 16) & 0xFF))
        b = int(((color >> 8) & 0xFF))
        a = int((color & 0xFF))
        colors_iterable.append((r,g,b,a))
    result:Surface = pykingdom.gradients.vertical((len(bitmap), len(bitmap[0])), colors_iterable[0], colors_iterable[1])
    pa = PixelArray(result)
    return pa