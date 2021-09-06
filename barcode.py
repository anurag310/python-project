import barcode
from barcode.writer import ImageWriter

text = "Python programming Code"
text1 = str(text)
code = barcode.get_barcode_class("code128")
image = code(text,writer=Imagewriter())
save_img = image.save('my final barcode')
