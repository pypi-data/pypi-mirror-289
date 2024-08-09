import cv2
import numpy as np
import mood_analysis.detection

video_capture = cv2.VideoCapture(0)

# 1. Emotion Detection 
#detection.emotion_detection(video_capture,cv2)

# 2. Face Detection 
mood_analysis.detection.face_detection(video_capture,cv2)

