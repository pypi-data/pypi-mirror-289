import os
from PIL import Image
import numpy as np
from pathlib import Path

from_path = './images'
to_path = './output'
##to_path2 = './bak'



pathlist = Path(from_path).glob("**/*.jpg")
print(pathlist)
for image_path in pathlist:
    print(image_path)
    img_name = os.path.basename(image_path)
    img = Image.open(image_path)
    if(img.mode != 'RGB'):
        img = img.convert("RGB")
    if(img.mode == 'RGB'):
        i = 1
        j = 1
        width = img.size[0]
        height = img.size[1]
        for i in range(0,width):#遍历所有长度的点
            for j in range(0,height):#遍历所有宽度的点
                data = (img.getpixel((i,j)))#打印该图片的所有点
                if (data[0]<= 127 or data[1]<=127 or data[2]<=127):#RGB值 越小越深
                    img.putpixel((i,j),(0,0,65,255))
        img.save(to_path +'/'+img_name)

##        img.save(to_path +'/'+img_name)
##    else:
##        img.save(to_path2 +'/'+img_name)
