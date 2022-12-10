import os
import shutil

def check_dir():
    curr_dir = os.getcwd()
    
    output_exist = os.path.exists(os.path.join(curr_dir , "Output"))

    if output_exist == False:
        path = os.path.join(curr_dir, "Output")
        os.mkdir(path)
    
    audio_exist = os.path.exists(os.path.join(curr_dir , "Output","Audio"))
    
    if audio_exist == False:
        path = os.path.join(curr_dir , "Output","Audio")
        os.mkdir(path)
    
    
    screenshots_exist = os.path.exists(os.path.join(curr_dir , "Output","Screenshots"))
    
    if screenshots_exist == False:
        path = os.path.join(curr_dir, "Output","Screenshots")
        os.mkdir(path)
        
        


def delete_dir():

    curr_dir = os.getcwd()

    output_exist = os.path.exists(os.path.join(curr_dir , "Output"))

    if output_exist == True:
        shutil.rmtree(os.path.join(curr_dir , "Output"))