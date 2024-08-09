import cv2
import face_recognition
import numpy as np
from deepface import DeepFace  
import math
import argparse
import logging

def face_detection(video_capture,cv2):

  # Face Detection variable declrations ***************************************

  # Load a sample picture and learn how to recognize it.
  obama_image = face_recognition.load_image_file("src/mood_analysis/files/obama.jpg")
  obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

  # Load a second sample picture and learn how to recognize it.
  biden_image = face_recognition.load_image_file("src/mood_analysis/files/biden.jpg")
  biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

  selva_image = face_recognition.load_image_file("src/mood_analysis/files/selva3.jpeg")
  selva_face_encoding = face_recognition.face_encodings(selva_image)[0]

  kanish_image = face_recognition.load_image_file("src/mood_analysis/files/kanish.jpeg")
  kanish_face_encoding = face_recognition.face_encodings(kanish_image)[0]

  narmathaa_image = face_recognition.load_image_file("src/mood_analysis/files/narmathaa.jpeg")
  narmathaa_face_encoding = face_recognition.face_encodings(narmathaa_image)[0]

  # Create arrays of known face encodings and their names
  known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding,
    selva_face_encoding,
    kanish_face_encoding,
    narmathaa_face_encoding
  ]
  known_face_names = [
    "Barack Obama",
    "Joe Biden",
    "Selva",
    "Kanish",
    "Narmathaa"
  ]
  # Initialize some variables
  face_locations = []
  face_encodings = []
  face_names = []
  process_this_frame = True
  face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
  # Age & Gender variable declrations ***************************************
  parser=argparse.ArgumentParser()
  parser.add_argument('--image')
  args=parser.parse_args()
  faceProto='src/mood_analysis/files/opencv_face_detector.pbtxt'
  faceModel='src/mood_analysis/files/opencv_face_detector_uint8.pb'
  ageProto="src/mood_analysis/files/age_deploy.prototxt"
  ageModel="src/mood_analysis/files/age_net.caffemodel"
  genderProto="src/mood_analysis/files/gender_deploy.prototxt"
  genderModel="src/mood_analysis/files/gender_net.caffemodel"

  MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)
  ageList=['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
  genderList=['Male','Female']

  logging.info('log'+faceProto)
  logging.info('This is an info message')


  faceNet=cv2.dnn.readNet(faceModel,faceProto)
  ageNet=cv2.dnn.readNet(ageModel,ageProto)
  genderNet=cv2.dnn.readNet(genderModel,genderProto)

  while True:

    # Emotion Detection part of the code***************************************
    # Grab a single frame of video
    ret, frame = video_capture.read()
    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Convert grayscale frame to RGB format
    rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))
    
    # Face Detection part of the code ***************************************
    if process_this_frame:
        
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)
            print(face_names)

    process_this_frame = not process_this_frame
    # Display the results

    # Emotion Detection part of the code ****************************************
        # Display the results
    for (x, y, w, h) in faces:
        # Extract the face ROI (Region of Interest)
        face_roi = rgb_frame[y:y + h, x:x + w]
        # Perform emotion analysis on the face ROI
        result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
        # Determine the dominant emotion
        emotion = result[0]['dominant_emotion']
        # # Draw rectangle around face and label with predicted emotion
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        print(emotion)
        
    # Face Detection part of the code ****************************************
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        print(name)

    # AgeGender part of the code ****************************************
    padding=20
    resultImg,faceBoxes=highlightFace(faceNet,frame)
    if not faceBoxes:
        print("No face detected")

    for faceBox in faceBoxes:
        face=frame[max(0,faceBox[1]-padding):
                   min(faceBox[3]+padding,frame.shape[0]-1),max(0,faceBox[0]-padding)
                   :min(faceBox[2]+padding, frame.shape[1]-1)]

        blob=cv2.dnn.blobFromImage(face, 1.0, (227,227), MODEL_MEAN_VALUES, swapRB=False)
        genderNet.setInput(blob)
        genderPreds=genderNet.forward()
        gender=genderList[genderPreds[0].argmax()]
        print(f'Gender: {gender}')

        ageNet.setInput(blob)
        agePreds=ageNet.forward()
        age=ageList[agePreds[0].argmax()]
        print(f'Age: {age[1:-1]} years')
        cv2.putText(frame, "           "+gender+"-"+age, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
        #cv2.putText(resultImg, f'{gender}, {age}', (faceBox[0], faceBox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2, cv2.LINE_AA)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   
# Release the capture and close all windows
  video_capture.release()
  cv2.destroyAllWindows()


def highlightFace(net, frame, conf_threshold=0.7):
    frameOpencvDnn=frame.copy()
    frameHeight=frameOpencvDnn.shape[0]
    frameWidth=frameOpencvDnn.shape[1]
    blob=cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)
    detections=net.forward()
    faceBoxes=[]
    for i in range(detections.shape[2]):
        confidence=detections[0,0,i,2]
        if confidence>conf_threshold:
            x1=int(detections[0,0,i,3]*frameWidth)
            y1=int(detections[0,0,i,4]*frameHeight)
            x2=int(detections[0,0,i,5]*frameWidth)
            y2=int(detections[0,0,i,6]*frameHeight)
            faceBoxes.append([x1,y1,x2,y2])
            cv2.rectangle(frameOpencvDnn, (x1,y1), (x2,y2), (0,255,0), int(round(frameHeight/150)), 8)
    return frameOpencvDnn,faceBoxes
