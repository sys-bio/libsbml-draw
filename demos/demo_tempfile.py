from pathlib import Path
import tempfile

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#NETWORK_IMAGE = "network_image.png"

NETWORK_IMAGE = "node_example_subplots_adjust.png"

with tempfile.TemporaryDirectory() as tmpdirname:

    file_path = Path(tmpdirname) / NETWORK_IMAGE
    
    print("file path: ", file_path)    

img = mpimg.imread(NETWORK_IMAGE)
plt.imshow(img)

plt.axis("off")

plt.show()
    
    



# fig.subplots_adjust(0,0,1,1)
    
# remove bbox_inches argument from savefig
    
# %config InlineBackend.print_figure_kwargs = {'bbox_inches':None}