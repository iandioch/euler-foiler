# euler-foiler

Do you want to get the number of Project Euler problems you have solved programmatically, without spoofing the login captcha? This is a tool to take your profile badge (visible at https://projecteuler.net/profiles/you.png), and use [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition) to parse the number of problems you have solved out of it.

You can run it on local file with `python3 parse.py -f path_to_badge.png` or have it download user's badge with `python3 parse.py -u username`.

It depends on [pyocr](https://github.com/jflesch/pyocr/), [tesseract-ocr](https://github.com/tesseract-ocr/tesseract), and of course, Python 3.

All contributions and comments are welcome. 

You can learn more about the project at [this blogpost about it](http://mycode.doesnot.run/2017/01/15/parsing-project-euler-progress/).
