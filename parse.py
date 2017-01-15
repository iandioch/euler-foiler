from PIL import Image
import sys

import pyocr
import pyocr.builders

image_loc = ' '.join(sys.argv[1:])

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("Error: No OCR tool found")
    sys.exit(1)

# should be 'Tesseract (sh)'
tool = tools[0]

orig_image = Image.open(image_loc)

# crop to only the section with the number of problems solved
cropped_image = orig_image.crop((47, 40, 97, 60))

# double the size of the image so the OCR has more to go on
resized_image = cropped_image.resize((100, 40), Image.ANTIALIAS)

digits = tool.image_to_string(
        resized_image,
        builder=pyocr.tesseract.DigitBuilder()
)

print(digits)
