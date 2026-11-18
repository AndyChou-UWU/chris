from PIL import Image,ImageDraw,ImageFont
im=Image.new('RGBA',(640,150));d=ImageDraw.Draw(im)
f=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',32)
d.rounded_rectangle((8,8,620,126),radius=28,fill=(13,57,72,235),outline=(255,212,70,255),width=5)
d.text((92,46),'BIG IDEAS, BRIGHT FUTURE!',font=f,fill='white')
d.regular_polygon((52,65,27),5,rotation=0,fill=(255,212,70))
im.save('fun_badge.png')
