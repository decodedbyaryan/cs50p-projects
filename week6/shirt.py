import sys
from PIL import Image
from PIL import ImageOps


if len(sys.argv) != 3:
    sys.exit("Invalid number of arguments")

if not sys.argv[1].lower().endswith(".jpg") and not sys.argv[1].lower().endswith(".png") and not sys.argv[1].lower().endswith(".jpeg"):
    sys.exit("Invalid file type")
    
if not sys.argv[2].lower().endswith(".jpg") and not sys.argv[2].lower().endswith(".jpeg") and not sys.argv[2].lower().endswith(".png"):
    sys.exit("Invalid file type")

if sys.argv[1].split(".")[-1].lower() != sys.argv[2].split(".")[-1].lower():
    sys.exit("Please enter same file type")

try:
    image = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    image = ImageOps.fit(image, shirt.size)
    image.paste(shirt, shirt)
    image.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("File does not exist")

