import requests
from io import BytesIO
from PIL import Image, ImageDraw,ImageFont,ImageFilter
from itertools import chain
import requests
from video_make import movie_to_image
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import numpy as np


    
def getRectangle(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']
    bottom = left + rect['height']
    right = top + rect['width']
    return ((left, top), (bottom, right))

def getAge(faceDictionary):
    f=faceDictionary['faceAttributes']
    age=f['age']
    return age
def getGender(faceDictionary):
    f=faceDictionary['faceAttributes']
    gender=f['gender']
    return gender

def getRectangle2(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']
    bottom = left + rect['height']
    right = top + rect['width']
    return (left,top,right,bottom)

def blurRegions(x,im,n):
    ic=im.crop(x)
    for i in range(n):
        ic=ic.filter(ImageFilter.GaussianBlur)     
    im.paste(ic,x)
    return im

def getEmotion(faceDictionary):
    f=faceDictionary['faceAttributes']
    emotion=f['emotion']
    anger=emotion['anger']
    contempt=emotion['contempt']
    disgust=emotion['disgust']
    fear=emotion['fear']
    happiness=emotion['happiness']
    neutral=emotion['neutral']
    sadness=emotion['sadness']
    surprise=emotion['surprise']
    list_of_emotions=np.array([anger,contempt,disgust,fear,happiness,neutral,sadness,surprise])
    index_max=np.argmax(list_of_emotions)
    return index_max



# Replace <Subscription Key> with your valid subscription key.
subscription_key = ""
assert subscription_key

# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
#
# Free trial subscription keys are generated in the westcentralus region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
vision_base_url = "https://japaneast.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=false"

analyze_url = vision_base_url + "analyze"

# Set image_path to the local path of an image that you want to analyze.
image_counter=0
image_counter2=0
while True:
        
    image_path = '/Users/dukeglacia/Downloads/test_images/%d.jpg'%image_counter
    image_counter+=1

    # Read the image into a byte array
    image_data = open(image_path, "rb").read()
    headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
                      'Content-Type': 'application/octet-stream'}
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,' +
        'emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
    }

    response = requests.post(
        analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()

    # The 'analysis' object contains various fields that describe the image. The most
    # relevant caption for the image is obtained from the 'description' property.
    analysis = response.json()
#         print(analysis)
        # image_caption = analysis["description"]["captions"][0]["text"].capitalize()

        # Display the image and overlay it with the caption.
    image = Image.open(BytesIO(image_data))
#         plt.imshow(image)
#         plt.axis("off")
#         plt.show()
        # _ = plt.title(image_caption, size="x-large", y=-0.1)
    draw = ImageDraw.Draw(image)
    for face in analysis:
        if getEmotion(face)==0:
            draw.rectangle(getRectangle(face), outline='red',fill=(255,0,0))
            draw.text(getRectangle(face)[0],str(getGender(face))+' '+str(getAge(face)), fill=(0, 0, 0))
        elif getEmotion(face)==1:
            draw.rectangle(getRectangle(face), outline='red',fill=(0,255,0))
            draw.text(getRectangle(face)[0],str(getGender(face))+' '+str(getAge(face)), fill=(255, 0, 0))
        elif getEmotion(face)==2:
            draw.rectangle(getRectangle(face), outline='red',fill=(127,0,255))
            draw.text(getRectangle(face)[0],str(getGender(face))+' '+str(getAge(face)), fill=(255, 0, 0))
        elif getEmotion(face)==3:
            draw.rectangle(getRectangle(face), outline='red',fill=(128,128,128))
            draw.text(getRectangle(face)[0],str(getGender(face))+' '+str(getAge(face)), fill=(255, 0, 0))
        elif getEmotion(face)==4:
            draw.rectangle(getRectangle(face), outline='red',fill=(255,255,0))
            draw.text(getRectangle(face)[0],str(getGender(face))+' '+str(getAge(face)), fill=(255, 0, 0))
        elif getEmotion(face)==5:
            draw.rectangle(getRectangle(face), outline='red',fill=(254,254,254))
            draw.text(getRectangle(face)[0],str(getGender(face))+' '+str(getAge(face)), fill=(255, 0, 0))
        elif getEmotion(face)==6:
            draw.rectangle(getRectangle(face), outline='red',fill=(153,76,0))
            draw.text(getRectangle(face)[0],str(getGender(face))+' '+str(getAge(face)), fill=(255, 0, 0))
        elif getEmotion(face)==7:
            draw.rectangle(getRectangle(face), outline='red',fill=(0,0,255))
            draw.text(getRectangle(face)[0],str(getGender(face))+' '+str(getAge(face)), fill=(255, 0, 0))
            
 
    image.save('/Users/dukeglacia/Downloads/test_images/%d.jpg'%image_counter2, 'JPEG', quality=100, optimize=True)
    image_counter2+=1
