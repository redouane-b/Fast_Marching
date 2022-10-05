import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd

Image=Image.open("OIP.png")
image_array=np.array(Image)
print(np.shape(image_array))

print(image_array)
plt.imshow( image_array )
plt.show()
n=np.shape(image_array)[0]
m=np.shape(image_array)[1]
h=4
nn=n//h
nm=m//h
FL=np.zeros((nn,nm))
for i in range(nn):
    for j in range(nm):
        m=0
        for ih in range(h):
            for jh in range(h):
                m+=255-(image_array[i*h+ih,j*h+jh,0]+image_array[i*h+ih,j*h+jh,1]+image_array[i*h+ih,j*h+jh,2])/3
        m=int(m/(h**2))

        if m<=200:
            FL[i,j]=0.001
        else :
            FL[i,j]=1


print(FL)


pd.DataFrame(FL)
plt.imshow(FL, cmap='hot', interpolation='nearest')
plt.show()