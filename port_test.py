# -*- coding: utf-8 -*-
import skt_face

imgpath = './26_1.jpg'
img = cv2.imread(imgpath)
phone_num = 5122
school_name = 'snu'

info = skt_face.call(phone_num, school_name, imgpath)

print info
# 아래와 같이 print가 찍히면 성공입니다.
# AICLOUD RDV SERVER     
#     DA3FA66F437C41479061992D8CF8A3C6
# {'faceLoc': {u'pointX': 82, u'pointY': 78, u'width': 123, u'height': 163}, 'name': u'\uae40\ucca0\uc218', 'conf': u'0.995581'}