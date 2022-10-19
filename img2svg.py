#img2svg.py
#Created by JGallo 2022/10/19
#Convert image files to .svg format

import aspose.words as aw
import argparse

parser = argparse.ArgumentParser(description='Convert image files to .svg format')
parser.add_argument('-i', '--input', help='Image file name')
args = parser.parse_args()

if(args.input == None):
    parser.print_help(file=None)
else:
    doc = aw.Document()
    builder = aw.DocumentBuilder(doc)
    shape = builder.insert_image(str(args.input))
    shape.image_data.save(str(args.input)[0:len(str(args.input))-4] + '.svg')
    
