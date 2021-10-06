#pip install Pillow

from PIL import Image
fails = Image.open('rudens.jpg')
fails.show()
fails.close()