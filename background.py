from PIL import Image
from noise import pnoise2
import numpy as np

class Background:
    def __init__(self, dimensions, octaves):
        self.dimensions = dimensions
        self.octaves = octaves

    def background(self):
        texture = np.empty([self.dimensions[1], self.dimensions[0]])
        freq = 16.0 * self.octaves

        for i in range(self.dimensions[1]):
            for j in range(self.dimensions[0]):
                v = int(pnoise2(i / freq, j / freq, self.octaves) * 127.0 + 128.0)
                texture[i][j] = v 

        return Image.fromarray(texture).convert("RGB") 
        
