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