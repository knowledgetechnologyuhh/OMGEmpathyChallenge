
import os
from shutil import copyfile

import subprocess



def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """
    import re
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    l.sort(key=alphanum_key)
    return l


def extractAudio(path, savePath):
    videos = os.listdir(path)

    for video in videos:
        videoPath = path + "/" + video

        if not os.path.exists(savePath):
            print "- Processing Video:", videoPath + " ..."
            os.makedirs(savePath)

        copyTarget = "/data/datasets/OMG-Empathy/clip1.mp4"
        print "--- Copying file:", videoPath + " ..."
        copyfile(videoPath, copyTarget)
        print "--- Extracting audio:", savePath + "/"+video+".wav" + " ..."
        command1 = "avconv -v quiet -i " + copyTarget + " -ab 160k -ac 1 -ar 16000 -vn " + savePath + "/"+video+".wav"
        subprocess.call(command1, shell=True)


    # for session in sessions:
    #
    #     dialogues = os.listdir(path + "/" + session)
    #
    #     for dialogue in dialogues:
    #         videoPath = path + "/" + session + "/" + dialogue
    #
    #         savePathAudio = savePath + "/" + session + "/" + dialogue
    #         if not os.path.exists(savePathAudio):
    #             print "- Processing Video:", videoPath + " ..."
    #             os.makedirs(savePathAudio)
    #
    #             copyTarget = "/data/datasets/OMG-Empathy/clip1.mp4"
    #             print "--- Copying file:", videoPath + " ..."
    #             copyfile(videoPath, copyTarget)
    #             print "--- Extracting audio:", savePathAudio + " ..."
    #             command1 = "avconv -v quiet -i " + copyTarget + " -ab 160k -ac 1 -ar 16000 -vn " + savePathAudio + "/audio.wav"
    #             subprocess.call(command1, shell=True)
    #
    #         else:
    #             print "Skip:", savePathAudio



if __name__ == "__main__":

    path ="/informatik3/wtm/datasets/KT Published Datasets/20182509_Empathy_Challenge_Barros/Dataset/Final_2/Validation/Videos/"
    savePath ="/data/datasets/OMG-Empathy/audio/Validation/"

    extractAudio(path,savePath)

