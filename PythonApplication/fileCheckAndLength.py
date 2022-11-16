import os

def checkFileExists():
    currDir = os.getcwd()
    
    
    audioExist = os.path.exists(currDir + "\Audio")
    
    if audioExist == False:
        return False
    
    
    screenshotsExist = os.path.exists(currDir + "\Screenshots")
    
    if screenshotsExist == False:
        return False
    return True

def noOfFiles():

    total = 0
    currDir = os.getcwd()
    
    audioDir = currDir + "\Audio"
    total += len(os.listdir(audioDir))

    screenshotDir = currDir + "\Screenshots"
    total += len(os.listdir(screenshotDir))

    return total

    
