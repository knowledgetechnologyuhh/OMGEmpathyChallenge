import cv2
import os
import dlib

import subprocess
import shutil
from shutil import copyfile
import sys


def progressBar(value, endvalue, bar_length=20):
    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length) - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\rPercent: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()


def extractFramesFromVideo(path,savePath, faceDetectorPrecision):
    videos = os.listdir(path + "/")

    for video in videos:

        videoPath = path + "/" + video
        print "- Processing Video:", videoPath + " ..."
        detector = dlib.get_frontal_face_detector()
        dataX = []

        copyTarget = "/data/datasets/OMG-Empathy/clip1.mp4"
        print "--- Copying file:", videoPath + " ..."
        copyfile(videoPath, copyTarget)
        cap = cv2.VideoCapture(copyTarget)

        #cap = cv2.VideoCapture(videoPath)
        totalFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        numberOfImages = 0
        check = True
        flag = True
        imageNumber = 0
        lastImageWithFaceDetected = 0
        print "- Extracting Faces:", str(totalFrames) + " Frames ..."

        savePathActor = savePath + "/" + video + "/Actor/"
        savePathSubject = savePath + "/" + video + "/Subject/"

        if not os.path.exists(savePathActor):
            os.makedirs(savePathActor)
            os.makedirs(savePathSubject)
            while (check):
                    check, img = cap.read()
                    if img is not None:

                        #Extract actor face
                        imageActor = img[0:720, 0:1080]
                        if lastImageWithFaceDetected == 0 or lastImageWithFaceDetected > faceDetectorPrecision:
                            dets = detector(imageActor, 1)
                            lastImageWithFaceDetected = 0
                            oldDetsActor = dets
                        else:
                            dets = oldDetsActor

                        try:
                            for i, d in enumerate(dets):
                                croped = imageActor[d.top():d.bottom(), d.left():d.right()]
                                cv2.imwrite(savePathActor + "/%d.png" % imageNumber, croped)

                        except:
                            print "------error!"

                        # Extract Subject Face
                        imageSubject = img[0:720, 1080:2560]
                        if lastImageWithFaceDetected == 0 or lastImageWithFaceDetected > faceDetectorPrecision:
                            dets = detector(imageSubject, 1)
                            lastImageWithFaceDetected = 0
                            oldDetsSubject = dets
                        else:
                            dets = oldDetsSubject

                        try:
                            for i, d in enumerate(dets):
                                croped = imageSubject[d.top():d.bottom(), d.left():d.right()]
                                cv2.imwrite(savePathSubject + "/%d.png" % imageNumber, croped)

                        except:
                            print "------error!"

                        imageNumber = imageNumber + 1
                        lastImageWithFaceDetected = lastImageWithFaceDetected + 1
                        progressBar(imageNumber, totalFrames)






if __name__ == "__main__":


    #Path where the videos are
    path ="/informatik3/wtm/datasets/KT Published Datasets/20182509_Empathy_Challenge_Barros/Dataset/Final_2/Validation/Videos/"

    #Path where the faces will be saved
    savePath ="/data/datasets/OMG-Empathy/faces_New_Validation/"

    # If 1, the face detector will act upon each of the frames. If 1000, the face detector update its position every 100 frames.
    faceDetectorPrecision = 1000

    detector = dlib.get_frontal_face_detector()

    extractFramesFromVideo(path, savePath, tempFolder)
