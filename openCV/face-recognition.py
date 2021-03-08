######################################################################################

# matplotlib 와 OpenCV 의 Drawing API 를 이용하여 화면에 여러 가지 도 형을 그려주는 코드

import cv2
import numpy as np
from matplotlib import pyplot as plt

#이미지 버퍼 생성
buffer = np.full((256,256,3), 255, np.uint8)

#이미지 버퍼 가공
#대각선
cv2.line(buffer,(0,0),(256,256),(255,0,0),5)
#사각형
cv2.rectangle(buffer,(182,100),(255,164),(0,255,0),3)
#이미지 버퍼 출력
plt.imshow(buffer)
plt.show()
######################################################################################
#Face-Detection을 해보자
from google.colab import drive
drive.mount('/gdrive')

#pip install face_recognition 실행

import cv2, os
import face_recognition as fr
from IPython.display import Image, display
from matplotlib import pyplot as plt
#이미지 가져오기
image_path = "/gdrive/My Drive/ggg1.jpg"
#얼굴 영역 추출
image = fr.load_image_file(image_path)
face_locations = fr.face_locations(image)
#얼굴영역 표시
for (top, right, bottom, left) in face_locations:
  cv2.rectangle(image, (left,top), (right,bottom), (0,255,0), 3)
#이미지 버퍼 출력
plt.rcParams["figure.figsize"] = (16,16)
plt.imshow(image)
plt.show()

######################################################################################
#얼굴인식으로 동일인을 찾아보자

plt.rcParams["figure.figsize"] = (1,1)

#이미지 파일을 로드하여 known_person_list 리스트 생성
known_person_list = []
known_person_list.append(fr.load_image_file("/gdrive/My Drive/colab/gangin.jpg"))
known_person_list.append(fr.load_image_file("/gdrive/My Drive/colab/jisung.jpg"))
known_person_list.append(fr.load_image_file("/gdrive/My Drive/colab/daeho.jpg"))
known_person_list.append(fr.load_image_file("/gdrive/My Drive/colab/heungmin.jpg"))

#기존 리스트에 없는 파일 연다

unknown_person = fr.load_image_file("/gdrive/My Drive/colab/heungmin.jpg")

#얼굴좌표를 알아내서 자른다
top,right,bottom,left = fr.face_locations(unknown_person)[0]
unknown_face = unknown_person[top:bottom, left:right]

#unknown_face 라는 타이틀을 붙여서 표시

plt.title("unknown_face")
plt.imshow(unknown_face)
plt.show()

# unknown_person_face 인코딩
enc_unknown_face = fr.face_encodings(unknown_face)

#등록된 얼굴리스트를 비교
for face in known_person_list:


  #등록된 얼굴을 129-dimensional face 인코딩
  enc_known_face = fr.face_encodings(face)

  #등록된 얼굴과 새로운 얼굴의 distance 얻기
  distance = fr.face_distance(enc_known_face ,enc_unknown_face[0])

  #distance 수치를 포함안 얼굴 출력
  plt.title("distance " + str(distance))
  plt.imshow(face)
  plt.show()
