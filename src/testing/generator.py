from datetime import date
from random import randint
from sys import argv
from PIL import Image, ImageFont, ImageDraw


class Generator:
	base_table_grid_size = (40, 20) 
	table_padding = 10
	text_padding = (10, 5)

	def make_tables(self, limit = 100):
		font = ImageFont.truetype("Arial.ttf", 12)	
		data = '['	
		rc_data = []
		for i in range(0, limit):
			rows = randint(2, 10)
			cols = randint(2, 10)
			contents, no_outer_borders = self._create_table(rows, cols, font, "./data/tables/{}.png".format(i))		
			data = data + str(contents).replace('\'', '\"') + ',\n'
			rc_data.append([rows, cols, not no_outer_borders])
		data = data[:-2] + ']'
		with open('./data/tables/data.json', 'w') as file:
			file.write(data)
		with open('./data/tables/props.csv', 'w') as file:
			file.write("index, rows, columns, outer_borders\n")
			for i in range(0, len(rc_data)):
				file.write("{}, {}, {}, {}\n".format(i, rc_data[i][0], rc_data[i][1], 1 if rc_data[i][2] else 0))			
		

	def _create_table(self, rows, columns, font, filename):
		# size = (Generator.base_table_grid_size[0] * columns + Generator.table_padding * 2,\
		# 	 rows * Generator.base_table_grid_size[1] + Generator.table_padding * 2)
		size = (500, 500)
		img = Image.new('RGB', size, "white")
		draw = ImageDraw.Draw(img)
		no_outer_borders = randint(0, 1) == 1 
		contents = []

		for r in range(0, rows):
			contents.append([])
			for c in range(0, columns):
				text = "{},{}".format(r,c)
				contents[r].append(text)
				x0 = c * Generator.base_table_grid_size[0] + Generator.table_padding
				y0 = r * Generator.base_table_grid_size[1] + Generator.table_padding
				x1 = (c + 1) * Generator.base_table_grid_size[0] + Generator.table_padding
				y1 = (r + 1) * Generator.base_table_grid_size[1] + Generator.table_padding
				draw.rectangle([x0,y0,x1,y1], outline=(0, 0, 0), width=2)
				draw.text((x0 + Generator.text_padding[0], y0 + Generator.text_padding[1]), text, fill=(0, 0, 0), font=font)			
		if no_outer_borders:
				draw.rectangle([Generator.table_padding, 0, size[0], Generator.table_padding + 2], fill=(255, 255, 255))
				draw.rectangle([Generator.table_padding, size[1] - Generator.table_padding - 2, size[0], size[1]], fill=(255, 255, 255))
				draw.rectangle([Generator.table_padding, 0, Generator.table_padding + 2, size[1]], fill=(255, 255, 255))
				draw.rectangle([size[0] - Generator.table_padding - 2, 0, size[0], size[1]], fill=(255, 255, 255))
		img.save(filename)		
		return contents, no_outer_borders


def main(function, count):
	gen = Generator()
	if function == 'tables':
		gen.make_tables(count)

if __name__ == "__main__":	
	main(argv[1], int(argv[2]))