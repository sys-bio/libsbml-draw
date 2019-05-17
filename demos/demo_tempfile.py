from pathlib import Path
import tempfile

NETWORK_IMAGE = "network_image.png"

with tempfile.TemporaryDirectory() as tmpdirname:

    file_path = Path(tmpdirname) / NETWORK_IMAGE
    
    
    