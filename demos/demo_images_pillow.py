# https://stackoverflow.com/questions/26649716/how-to-show-pil-image-in-ipython-notebook

## 
## Option 1
##

from PIL import Image                 # to load images
from IPython.display import display   # to display images

im = Image.open("complicated_nodes.png")

display(im)

# opens ImageMagick
# im.show()

print(im.format, im.size, im.mode)

out = im.resize((1000, 1000))
type(out)
display(out)


## 
## Option 2
##

from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image

#%matplotlib inline
pil_im = Image.open("complicated_nodes.png", 'r')
imshow(np.asarray(pil_im))
# unknown property width
#imshow(np.asarray(pil_im), width=1000, height=1000)
#imshow(random.rand(8, 90), interpolation='nearest', aspect='auto')

## 
## Option 3
##

# from IPython.display import Image 
# Image(filename="complicated_nodes.png")
from IPython.display import Image 
im = Image(filename="complicated_nodes.png", width=500, height=500)
type(im)
display(im)


#from PIL import Image               # to load images
#from IPython.display import display # to display images

#pil_im = Image.open("complicated_nodes.png")
#display(pil_im)

## ------------------------------
# To see methods:
# -------------------------------
# PIL.Image.Image.tab
