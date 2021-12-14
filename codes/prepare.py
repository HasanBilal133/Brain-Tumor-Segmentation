import os
import shutil
import random

imagePth = r'C:\Users\Hasan\Downloads\Compressed\Task01_BrainTumour\imagesTr\\'
labelPth = r'C:\Users\Hasan\Downloads\Compressed\Task01_BrainTumour\labelsTr\\'

imageTr = os.listdir(imagePth)
print(len(imageTr))

imageVal = r'C:\Users\Hasan\Downloads\Compressed\Task01_BrainTumour\imagesVal\\'
labelVal = r'C:\Users\Hasan\Downloads\Compressed\Task01_BrainTumour\labelsVal\\'

for i in range(50):
    element = random.choice(imageTr)
    shutil.move(imagePth+element, imageVal+element)
    shutil.move(labelPth+element, labelVal+element)
    imageTr.remove(element)

print(len(imageTr))


imageTs = r'C:\Users\Hasan\Downloads\Compressed\Task01_BrainTumour\imagesTs\\'
labelTs = r'C:\Users\Hasan\Downloads\Compressed\Task01_BrainTumour\labelsTs\\'

for i in range(34):
    element = random.choice(imageTr)
    shutil.move(imagePth+element, imageTs+element)
    shutil.move(labelPth+element, labelTs+element)
    imageTr.remove(element)

print(len(imageTr))













