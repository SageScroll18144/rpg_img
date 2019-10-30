import cv2
import os
import random as rd

#Nome da pasta
file = input("Informa aê o nome da pasta(obs: o programa é Case-sensitive).: ")

queue = []

for i in os.listdir(os.path.abspath(file)):
    queue.append(i)

img = cv2.imread(os.path.abspath(file)+'/'+queue[rd.randint(0,(len(queue)-1))])
cv2.imshow("RPG man?", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
