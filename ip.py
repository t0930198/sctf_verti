from PIL import Image
import urllib2
from StringIO import StringIO
import base64
from HTMLParser import HTMLParser

# pixel (w,h)
# red = (255,0,0)
# purple = (128, 0 ,128)
# blue = (0,0,255)
# green = (0,128,0)
# yellow = (255,255,0)
# orange = (255,165,0)
color = [(255,0,0)
        ,(128,0,128)
        ,(0,0,255)
        ,(0,128,0)
        ,(255,255,0)
        ,(255,165,0)
        ,(255,255,255)
        ,(0,0,0)]
color_len = 84
offset = 12
temp = []
def getColor(w,h):
    for i in color:
        if(img.getpixel((w,h)) == i):
            return int(color.index(i))
def getBinary(index):
    binary = ""
    for i in range(7):
        if(getColor(color_len+i*offset,index*offset)==7):
            binary+="1"
        elif(getColor(color_len+i*offset,index*offset)==6):
            binary+="0"
        # print binary
    return int(binary,2)
def main():
    for i in range(h):
            temp.append(getBinary(i)-getColor(0,i*offset))
    ans = ''.join(chr(j) for j in temp)
    return (ans)
# img = Image.open("B-Code.png")
# img = Image.open("")
img = Image.new( "RGB", (400,300) )
time = 0
w = 0
h = 0
stat="INCORRECT"
while (stat=="INCORRECT"):
    temp = []
    time+=1
    response = urllib2.urlopen("http://problems1.2016q1.sctf.io:50000/")
    content = response.read()
    imgData = content.split("base64,")[1].split("'>")[0];
    stat = content.split("<br>")[2]
    imgdata = base64.b64decode(imgData)
    fake_file = StringIO()
    fake_file.write(imgdata)
    img = Image.open(fake_file)
    w = img.size,img.size[0]/offset
    h = img.size[1]/offset
    ans = main()
    if("flag" in ans):
        print ans
    if(stat == "CORRECT"):
        print ans
print stat
# main()
