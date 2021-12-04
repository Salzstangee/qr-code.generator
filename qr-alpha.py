from os import remove, sysconf_names
import qrcode
import time
from PIL import Image 





while True:
  Link = input("Paste Link:")
  img = qrcode.make(Link)
  ImageName = input("Enter Image Name:")
  type(img);  # qrcode.image.pil.PilImage
  img.save(ImageName + ".png")
  im = Image.open (ImageName + ".png")
  im.show()
  print("succses!")
  print("your QR code has been saved as " + ImageName + ".png")
  time.sleep(2)


  Join = input('Would you like to restart? (Y/N)').lower()
  if Join.startswith('y'):
    print("Great,")
    continue
  else:
    print ("Sorry for asking...")
    break
