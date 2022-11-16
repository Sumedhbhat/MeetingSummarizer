import os
import shutil

def deleteDir():

    currDir = os.getcwd()

    audioExist = os.path.exists(currDir + "\Audio")

    if audioExist == True:
        shutil.rmtree(currDir + "\Audio")

    scExist = os.path.exists(currDir + "\Screenshots")

    if scExist == True:
        shutil.rmtree(currDir + "\Screenshots")
