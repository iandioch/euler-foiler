from PIL import Image
from io import BytesIO
import argparse
import urllib.request
import sys
import os

import pyocr
import pyocr.builders

def fetch_image(image_loc):
	with urllib.request.urlopen(image_loc) as req:
		if req.getcode() != 200:
			raise ConnectionError(req.getcode())
		return Image.open(BytesIO(req.read()))

def open_image(image_loc):
	if not len(image_loc):
		raise ValueError("Filename not specified")
	if not os.path.isfile(image_loc):
		raise FileNotFoundError(image_loc)
	return Image.open(image_loc)

def parse(orig_image):
	tools = pyocr.get_available_tools()
	if len(tools) == 0:
		return "Error: No OCR tool found"

	# should be 'Tesseract (sh)'
	tool = tools[0]

	# crop to only the section with the number of problems solved
	cropped_image = orig_image.crop((47, 40, 97, 60))

	# double the size of the image so the OCR has more to go on
	resized_image = cropped_image.resize((100, 40), Image.ANTIALIAS)

	digits = tool.image_to_string(
		resized_image,
		builder=pyocr.tesseract.DigitBuilder())

	return digits

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Parses Project Euler badge to extract number of problems solved.")
	source = parser.add_mutually_exclusive_group(required=True)
	source.add_argument('-f', '--file', type=str, help="Path to a local file")
	source.add_argument('-l', '--url', '--link', type=str, help="Image URL")
	source.add_argument('-u', '--user', '--username', type=str, help="Username to lookup")
	args = parser.parse_args()
	if args.file:
		print(parse(open_image(args.file)))
	elif args.url:
		print(parse(fetch_image(args.url)))
	elif args.user:
		print(parse(fetch_image("https://projecteuler.net/profile/{}.png".format(urllib.parse.quote(args.user)))))
	else:
		parser.error("No source specified")
