import cv2
import os
import random as rd

#Nome da pasta

def path(file):
    return os.path.abspath(file)

moves = open(path('path.txt'), 'r')
file =''

for i in moves:
    file = i
file = file.translate({ord('\n'): None})
queue = []

for i in os.listdir(file):
    queue.append(i)

img = cv2.imread(os.path.abspath(file)+'/'+queue[rd.randint(0,(len(queue)-1))])
cv2.imshow("RPG man?", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
