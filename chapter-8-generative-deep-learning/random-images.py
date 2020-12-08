import random

import imageio

random_factor = 100
img = []
aux = 0
for i in range(300):
    img.append([])
    for _ in range(300):
        aux += 2
        if aux > 255:
            aux = 0
        img[i].append([random.randint(max(aux-random_factor, 0), min(aux+random_factor, 255)), random.randint(
            max(aux-random_factor, 0), min(aux+random_factor, 255)), random.randint(max(aux-random_factor, 0), min(aux+random_factor, 255))])
imageio.imwrite('random-image.jpg', img)
