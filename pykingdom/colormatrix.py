# from http://www.quasimondo.com/colormatrix/ColorMatrix.as

LUMA_R = 0.212671
LUMA_G = 0.71516
LUMA_B = 0.072169

IDENTITY = [
    1, 0, 0, 0, 0,
    0, 1, 0, 0, 0,
    0, 0, 1, 0, 0,
    0, 0, 0, 1, 0
]

class ColorMatrix:

    def __init__(self):
        self.reset()

    def reset(self):
        self.matrix = IDENTITY

    def concat(self, mat:[]):
        temp = [] #24
        i = 0
        for y in range(4):
            for x in range(5):
                temp[i + x] = mat[i] * self.matrix[x] + \
                            mat[i+1] * self.matrix[x + 5] + \
                            mat[i+2] * self.matrix[x + 10] + \
                            mat[i+3] * self.matrix[x + 15] + \
                            (mat[i+4] if x == 4 else 0)
            i += 5
        self.matrix = temp

    def colorize(self, rgb:int, amount:int = 1):
        r = (((rgb >> 16) & 0xFF) / 0xFF)
        g = (((rgb >> 8) & 0xFF) / 0xFF)
        b = ((rgb & 0xFF) / 0xFF)
        inv_amount = 1 - amount

        self.concat([(inv_amount + ((amount * r) * LUMA_R)), ((amount * r) * LUMA_G), ((amount * r) * LUMA_B), 0, 0,
            		((amount * g) * LUMA_R), (inv_amount + ((amount * g) * LUMA_G)), ((amount * g) * LUMA_B), 0, 0,
            		((amount * b) * LUMA_R), ((amount * b) * LUMA_G), (inv_amount + ((amount * b) * LUMA_B)), 0, 0,
            		0, 0, 0, 1, 0])

    def adjust_contrast(self, r:int, g:int = None, b:int = None):
        if g == None: g = r
        if b == None: b = r
        r += 1
        g += 1
        b += 1

        self.concat([r, 0, 0, 0, (128 * (1 - r)),
					0, g, 0, 0, (128 * (1 - g)),
					0, 0, b, 0, (128 * (1 - b)),
					0, 0, 0, 1, 0])

    def adjust_saturation(self, s:int):
        sInv = 1 - s
        irlum = sInv * LUMA_R
        iglum = sInv * LUMA_G
        iblum = sInv * LUMA_B

        self.concat([(irlum + s), iglum, iblum, 0, 0,
            		irlum, (iglum + s), iblum, 0, 0,
            		irlum, iglum, (iblum + s), 0, 0,
            		0, 0, 0, 1, 0])