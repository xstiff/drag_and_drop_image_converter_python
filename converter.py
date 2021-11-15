from PIL import Image
import os
import time
import ctypes
import sys

path_list = sys.argv[1:]
path = ''
for p in path_list: path += p

if path == '':
        print("Drag and drop image onto python file")
        time.sleep(1.3)
        exit()
path = os.path.split(path)
path = path[1]

im = Image.open(open(path,'rb'))

rgb = im.convert('RGB')

y = input("Convert to: PNG\JPEG\JPG\GIF\WEBP\n")

output_file = 'output.' + y
rgb = im.save(output_file)

ctypes.windll.user32.MessageBoxW(0,f"{output_file} saved!", "Done")
exit()