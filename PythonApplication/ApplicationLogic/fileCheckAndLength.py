import os

def check_file_exists():
    curr_dir = os.getcwd()

    audio_exist = os.path.exists(os.path.join(curr_dir,'Output','Audio'))
    
    if audio_exist == False:
        return False
    
    screenshots_exist = os.path.exists(os.path.join(curr_dir,'Output','Screenshots'))
    
    if screenshots_exist == False:
        return False
    return True

def no_of_files():

    total = 0
    curr_dir = os.getcwd()

    screenshot_dir = os.path.join(curr_dir,'Output','Screenshots')
    total += len(os.listdir(screenshot_dir))

    audio_dir= os.path.join(curr_dir,'Output','Audio')
    total += len(os.listdir(audio_dir))

    return total