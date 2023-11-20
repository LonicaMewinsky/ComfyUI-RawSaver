import os
import sys
import subprocess

here = os.path.dirname(__file__)
requirements_path = os.path.join(here, "requirements.txt")

try:
    from .nodes.rawsaver import SaveTifImage
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_path])
    from .nodes.rawsaver import SaveTifImage

NODE_CLASS_MAPPINGS = {
    "SaveTifImage": SaveTifImage,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SaveTifImage": "SaveTifImage",
}