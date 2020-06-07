from PIL import Image
from noise import pnoise2
import numpy as np

class Background:
    def __init__(self, dimensions, octaves):
        self.dimensions = dimensions
        self.octaves = octaves

    def image(self):
        white = Image.new("RGB", self.dimensions, (255, 255, 255))
        texture = self.texturize()
        return Image.blend(white, texture, 0.1)

    def texturize(self):
        texture = np.empty([self.dimensions[0], self.dimensions[1]])
        freq = 16.0 * self.octaves

        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                v = int(pnoise2(i / freq, j / freq, self.octaves) * 127.0 + 128.0)
                texture[i][j] = v 

        return Image.fromarray(texture).convert("RGB") 
        

if __name__  == "__main__":
    bg = Background((1000,1000), octaves=6)
    im = bg.image()
    im.show()
