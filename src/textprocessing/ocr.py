from PIL import Image
import pytesseract as pt
import pandas as pd


def read_image(image_path: str) -> pd.DataFrame:
	image = Image.open(image_path)
	return pt.image_to_data(image, output_type=pt.Output.DATAFRAME)	