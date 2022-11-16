import os

def checkDir():
    currDir = os.getcwd()
    
    
    audioExist = os.path.exists(currDir + "\Audio")
    
    if audioExist == False:
        path = os.path.join(currDir, "Audio")
        os.mkdir(path)
    
    
    screenshotsExist = os.path.exists(currDir + "\Screenshots")
    
    if screenshotsExist == False:
        path = os.path.join(currDir, "Screenshots")
        os.mkdir(path)
