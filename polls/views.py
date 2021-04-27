from django.shortcuts import render
from io import StringIO
from .hindiCharacterRecognition import HindiCharacterRecognition
from PIL import Image
import re
import base64
import io
import numpy as np
import skimage.io
import cv2 as cv



# Create your views here.
def canvas(request):
    print("hello")
    return render(request,'canvas.html')   



def savecanvas(request):
    
    canvasData =request.POST.get('inp1')

    datauri = canvasData
    print(datauri)
    imgstr = re.search(r'base64,(.*)', datauri).group(1)
    print(imgstr)
    base64_decoded = base64.b64decode(imgstr)
    img = skimage.io.imread(io.BytesIO(base64_decoded),as_gray=True)
    img = cv.resize(img, dsize=(28, 28))
    #print(img)
    obj=HindiCharacterRecognition()
    res =obj.predictor(img)
    #print(res)
    return render(request,'canvas.html',{"ans":res})
