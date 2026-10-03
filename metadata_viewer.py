
"""Safe local-only image metadata viewer.

This utility reads metadata from a user-provided local image if Pillow is installed.
The image is not uploaded or stored by the web application.
"""
from pathlib import Path

def inspect_image(path):
    try:
        from PIL import Image
    except ImportError:
        raise RuntimeError("Install Pillow separately to use this optional utility.")
    p=Path(path)
    with Image.open(p) as img:
        exif=img.getexif()
        return {str(k): str(v) for k,v in exif.items()}
