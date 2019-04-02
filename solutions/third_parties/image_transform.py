from PIL import Image

image = Image.open('../../resources/strangerthings_cover.jpg')

image = image.crop((850, 200, 1160, 580))
image = image.convert('L')
image = image.transpose(Image.FLIP_LEFT_RIGHT)
image = image.resize((250, 300))
