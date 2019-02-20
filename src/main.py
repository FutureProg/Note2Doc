assert __name__ == '__main__'

import argparse
import textprocessing.ocr as ocr
import pandas as pd

parser = argparse.ArgumentParser(description="Execute Document Processing")
parser.add_argument('--image', help="The image to process", default="./test_doc.jpg")
args = parser.parse_args()

data: pd.DataFrame = ocr.read_image(args.image) 
print(data.head(15))

data = data.dropna(axis=0)['text']
print(' '.join(data.head(20).values))