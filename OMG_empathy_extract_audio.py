
import os


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

    videos = sort_nicely(os.listdir(path + "/"))

    for v in videos:

        utterances = sort_nicely(os.listdir(path + "/" + v + "/video"))

        for ut in utterances:


            savepath = savePath + v+ "/audio/"+ut +"/"

            print "Reading: ", path+"/"+v + "/video/" + ut
            print "Saving:", savepath

            if not os.path.exists(savepath):

                os.makedirs(savepath)
                command1 = "avconv -i " + path+"/"+v + "/video/" + ut + " -ab 160k -ac 1 -ar 16000 -vn " + savepath+"/audio.wav"
                print "Command:", command1
                subprocess.call(command1, shell=True)


            else:
                print "Skip:", savepath

if __name__ == "__main__":


    path ="/data/datasets/OMG-Emotion/OMG_Videos/"
    savePath ="/data/datasets/OMG-Emotion/audio_extraced_all/"

    extractAudio(path,savePath)

