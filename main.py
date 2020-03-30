from parse import *
from matrix import *
from graphics import *
import random

edgeMat = newMatrix(4,0)
polyMat = newMatrix(4,0)

transform = identity(newMatrix())
color = [0, 0, 0]
createPixels(800, 800, 255)
# parseFile("test", points, transform, pixels, color)
parseFile("script", edgeMat, polyMat, transform, pixels, color)
# Uncomment if you want to make the image
# parseFile("quarantine", points, transform, pixels, color)
