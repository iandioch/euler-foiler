from PIL import Image
import sys
import os

import pyocr
import pyocr.builders

def parse(image_loc):
	if not len(image_loc):
		return """Please provide a Project Euler badge png to parse.
As an example, to parse `test.png`, run the program like this:
python3 parse.py test.png"""

	if not os.path.isfile(image_loc):
		return ('Could not find a file with the given path: %s' % image_loc)

	tools = pyocr.get_available_tools()
	if len(tools) == 0:
		return "Error: No OCR tool found"

	# should be 'Tesseract (sh)'
	tool = tools[0]

	orig_image = Image.open(image_loc)

	# crop to only the section with the number of problems solved
	cropped_image = orig_image.crop((47, 40, 97, 60))

	width, height = cropped_image.size
	scale = 5

	# double the size of the image so the OCR has more to go on
	resized_image = cropped_image.resize((width*scale, height*scale), Image.ANTIALIAS)

	digits = tool.image_to_string(
		resized_image,
		builder=pyocr.tesseract.DigitBuilder())

	return digits

image_loc = ' '.join(sys.argv[1:])

print(parse(image_loc))

