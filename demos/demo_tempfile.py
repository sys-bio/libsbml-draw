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

# where add ipython config
# C:\Tellurium-Winpython-3.6\settings\.ipython\profile_default

# c.InlineBackend.rc = {}
# .ipython/profile_default/ipython_config.py
# Although for other users, the file might be located at:

# .config/ipython/profile_default/ipython_config.py
# If the config file doesn't exist, run this command to create it:
# ipython profile create

