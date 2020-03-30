from parse import *
from matrix import *
from graphics import *
import random

edgeMat = newMatrix(4,0)
polyMat = newMatrix(4,0)

transform = identity(newMatrix())
color = [80, 175, 60]
createPixels(600, 600, 255)
parseFile("script", edgeMat, polyMat, transform, pixels, color)
# Uncomment if you want to make the image
# parseFile("memes", edgeMat, polyMat, transform, pixels, color)
