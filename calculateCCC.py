from __future__ import print_function
import argparse
import os

from scipy.stats import pearsonr
import numpy
import pandas


def mse(y_true, y_pred):
    from sklearn.metrics import mean_squared_error
    return mean_squared_error(y_true,y_pred)

def f1(y_true, y_pred):
    from sklearn.metrics import f1_score
    label = [0,1,2,3,4,5,6]
    return f1_score(y_true,y_pred,labels=label,average="micro")

def ccc(y_true, y_pred):
    true_mean = numpy.mean(y_true)
    true_variance = numpy.var(y_true)
    pred_mean = numpy.mean(y_pred)
    pred_variance = numpy.var(y_pred)

    rho,_ = pearsonr(y_pred,y_true)

    std_predictions = numpy.std(y_pred)

    std_gt = numpy.std(y_true)

    ccc = 2 * rho * std_gt * std_predictions / (
        std_predictions ** 2 + std_gt ** 2 +
        (pred_mean - true_mean) ** 2)

    return ccc, rho

def orderFiles (folder):
    dataList = os.listdir(folder)

    dataList = sorted(sorted(dataList, key=lambda x: int(x.split(".")[0].split("_")[3])), key=lambda x: int(x.split(".")[0].split("_")[1]))


    return dataList


def calculateCCC(validationFolder, modelOutputFolder):

    validationFiles = orderFiles(validationFolder)
    modelOutputfolder = orderFiles(modelOutputFolder)


    cccList = []

    subjectCCC = []

    storyList = []
    subjectList = []

    currentSubject = validationFiles[0].split(".")[0].split("_")[1]
    for fileIndex in range (len(validationFiles)):

        subject = int(validationFiles[fileIndex].split(".")[0].split("_")[1])
        story = int(validationFiles[fileIndex].split(".")[0].split("_")[3])


        if not subject in subjectList:
            subjectList.append(subject)

        if not story in storyList:
            storyList.append(story)

        dataY = pandas.read_csv(validationFolder+"/"+validationFiles[fileIndex], header=0, sep=",")

        dataYPred = pandas.read_csv(modelOutputFolder+"/"+modelOutputfolder[fileIndex], header=0, sep=",")

        dataYValence = dataY["valence"]

        dataYPredValence = dataYPred["valence"]

        valenceCCC, vcor = ccc(dataYValence, dataYPredValence)

        subjectNumber = validationFiles[fileIndex].split(".")[0].split("_")[1]


        if subjectNumber == currentSubject:
            subjectCCC.append(valenceCCC)
        else:
            cccList.append(subjectCCC)
            subjectCCC = []
            subjectCCC.append(valenceCCC)
            currentSubject = subjectNumber


    cccList.append(subjectCCC)


    print("-----------Final Results-----------")
    phrase1 = "Subjects  | "
    for i in range(len(cccList[0])):
        phrase1 = phrase1 + "Story "+str(storyList[i])+ " | "

    print (phrase1)


    for i in range (len(cccList)):
        phrase2 = "Subject "+str(subjectList[i]) + " | "
        for j in range (len(cccList[i])):
            phrase2 = phrase2 + "{:.2f}".format(cccList[i][j])  + "    | "

        print (phrase2)

    print ("")
    print("")
    print("----------- Personalized Track-----------")
    meanCCCPersonalized = numpy.array(cccList).mean(axis=1)

    for i in range(len(meanCCCPersonalized)):
        print("Subject " + str(subjectList[i]) + " | " + "{:.2f}".format(meanCCCPersonalized[i]))

    print ("-----------------")
    print ("Mean      |", "{:.2f}".format(numpy.array(meanCCCPersonalized).mean()))
    print("-----------------")

    print("")
    print("")
    print("----------- Generalized Track-----------")
    meanCCCPersonalized = numpy.array(cccList).mean(axis=0)

    for i in range(len(meanCCCPersonalized)):
        print("Story " + str(storyList[i]) + " | " + "{:.2f}".format(meanCCCPersonalized[i]))

    print("---------------")
    print("Mean    |", "{:.2f}".format(numpy.array(meanCCCPersonalized).mean()))
    print("---------------")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("validationFolder")
    parser.add_argument("modelOutputFolder")

    opt = parser.parse_args()

    calculateCCC(opt.validationFolder, opt.modelOutputFolder)