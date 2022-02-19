import pathlib

TESSDATA_DIR = pathlib.Path.home() / 'tessdata'

TESSDATA_URL = 'https://github.com/tesseract-ocr/tessdata_fast/blob/main/{}.traineddata?raw=true'

TESSDATA_SCRIPT_URL = 'https://github.com/tesseract-ocr/tessdata_best/blob/main/script/{}.traineddata?raw=true'
