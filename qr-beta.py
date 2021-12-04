from os import remove, sysconf_names
import qrcode
import time
from PIL import Image 
import uuid


while True:
  filename = str(uuid.uuid4())
  Link = input("Paste Link:")
  img = qrcode.make(Link)
  type(img);  # qrcode.image.pil.PilImage
  img.save(filename + ".png")
  im = Image.open (filename + ".png")
  im.show()
  print("succses!")
  print("your QR code has been saved as " + filename + ".png")
  time.sleep(2)


  Join = input('Would you like to restart? (Y/N)').lower()
  if Join.startswith('y'):
    print("Great,")
    continue
  else:
    print ("Sorry for asking...")
    break