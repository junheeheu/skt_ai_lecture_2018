import cv2
import skt_face

imgpath = './26_1.jpg'
img = cv2.imread(imgpath)
phone_num = 5122
school_name = 'snu'

info = skt_face.call(phone_num, school_name, imgpath)

print('name: ', info['name'])
print('face location: ', info['faceLoc'])
print('conf: ', info['conf'])