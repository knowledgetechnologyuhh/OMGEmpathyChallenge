import cv2
import os
import dlib

import subprocess
import shutil
from shutil import copyfile
import sys

def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """
    import re
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    l.sort(key=alphanum_key)
    return l

def splitFrames(emotion, videoPath, tempFolder):
    shutil.rmtree(tempFolder)
    os.makedirs(tempFolder)

    copyTarget = "/data/datasets/OMG-Empathy/clip1.mp4"
    print "--- Copying file:", videoPath + " ..."
    copyfile(videoPath,copyTarget)
    print "--- Extracting frames:", videoPath + " ..."
    command1 = "avconv -v quiet -i " + copyTarget + " " + tempFolder + "/videoframe%d.png"
    #print "Command:", command1
    #raw_input("here")
    subprocess.call(command1, shell=True)
    os.remove(copyTarget)

def progressBar(value, endvalue, bar_length=20):
    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length) - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\rPercent: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()



def extractFrames(path, savePath, tempFolder, batch=""):

    sessions = os.listdir(path + "/" + batch)

    for session in sessions:

        dialogues = os.listdir(path + "/" + batch + session)

        for dialogue in dialogues:

            videoPath = path + "/" + session + "/" + dialogue

            savePathActor = savePath +  "/"+session+"/"+dialogue+ "/Actor/"
            savePathSubject = savePath + "/" + session + "/" + dialogue + "/Subject/"


            if not os.path.exists(savePathActor):
                print "- Processing Video:", savePathActor + " ..."

                os.makedirs(savePathActor)
                os.makedirs(savePathSubject)
                imageNumber = 0
                lastImageWithFaceDetected = 0
                splitFrames(batch, videoPath, tempFolder)

                totalFrames = len(os.listdir(tempFolder))

                print "- Extracting Faces:", str(totalFrames) + " Frames ..."
                numberOfFaces = 0
                for image in sort_nicely(os.listdir(tempFolder)):

                    img = cv2.imread(tempFolder + "/" + image)

                    #Extract Actor Face
                    imageActor = img[0:720,0:1080]
                    #cv2.imwrite("/data/datasets/OMG-Empathy/actor.png", imageActor)

                    if lastImageWithFaceDetected == 0 or lastImageWithFaceDetected > 10:
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


                    #Extract Subject Face
                    imageSubject = img[0:720, 1080:2560]
                    if lastImageWithFaceDetected == 0 or lastImageWithFaceDetected > 10:
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
            else:
                print "Skip:", videoPath




if __name__ == "__main__":

    tempFolder = "/data/datasets/OMG-Empathy/temp/"

    path ="/informatik2/wtm/datasets/KT Published Datasets/20182509_Empathy_Challenge_Barros/Dataset/Stitched/"
    savePath ="/data/datasets/OMG-Empathy/faces/"

    batches = sorted(os.listdir(path))
    detector = dlib.get_frontal_face_detector()

    for batch in batches:
        extractFrames(path, savePath, tempFolder)
