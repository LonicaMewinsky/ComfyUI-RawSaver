import torch
import numpy as np
import os
import imageio
import folder_paths

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class SaveTifImage:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"
        self.prefix_append = ""

    @classmethod
    def INPUT_TYPES(s):
        return {"required": 
                    {"images": ("IMAGE", ),
                     "filename_prefix": ("STRING", {"default": "ComfyUI"})},
                }

    RETURN_TYPES = ()
    FUNCTION = "save_tif_images"

    OUTPUT_NODE = True

    CATEGORY = "image"

    def save_tif_images(self, images, filename_prefix="ComfyUI"):
        filename_prefix += self.prefix_append
        full_output_folder, filename, counter, subfolder, filename_prefix = folder_paths.get_save_image_path(filename_prefix, self.output_dir, images[0].shape[1], images[0].shape[0])
        for image in images:
            nimg = image.cpu().numpy()
            nimg = np.float16(nimg)
            file = f"{filename}_{counter:05}_.tif"
            nimg = (nimg * 65535).astype(np.uint16)
            imageio.imwrite(os.path.join(full_output_folder, file), nimg)
            counter += 1

        return {"images": None}