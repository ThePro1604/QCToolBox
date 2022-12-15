<<<<<<< HEAD
import cv2
from matplotlib import pyplot as plt
import numpy as np

rows = 1
columns = 2
y2Points = np.array([12, 7, 6, 5, 4, 3, 2, 2, 1, 12])
Image1 = cv2.imread(r'C:\Users\shahaf.stossel\Downloads\banner-quality-control-vector-illustration-260nw-1339349438.png')

fig = plt.figure(figsize=(10, 7))
fig.add_subplot(rows, columns, 1)

plt.imshow(Image1)
plt.axis('off')
plt.title("First")

# Adds a subplot at the 2nd position
fig.add_subplot(rows, columns, 2)

# showing image
plt.imshow(Image1)
plt.axis('off')
plt.title("Second")
=======
from Tools.DoubleDisplay import ToolRun_DoubleDisplay
from Tools.Duplicator import ToolRun_Duplicator
from Tools.ExcelCells2Files import ToolRun_ExcelCells2Files
from Tools.PickleDumpMapper import ToolRun_PickleDumpMapper

ToolRun_DoubleDisplay()
ToolRun_Duplicator()
ToolRun_ExcelCells2Files()

ToolRun_PickleDumpMapper()
>>>>>>> 84b359e (Initial commit)
