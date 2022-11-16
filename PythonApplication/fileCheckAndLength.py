import os

def check_file_exists():
    curr_dir = os.getcwd()
    
    
    audio_exist = os.path.exists(curr_dir + "\Output\Audio")
    
    if audio_exist == False:
        return False
    
    
    screenshots_exist = os.path.exists(curr_dir + "\Output\Screenshots")
    
    if screenshots_exist == False:
        return False
    return True

def no_of_files():

    total = 0
    curr_dir = os.getcwd()
    
    audio_dir = curr_dir + "\Output\Audio"
    total += len(os.listdir(audio_dir))

    screenshot_dir = curr_dir + "\Output\Screenshots"
    total += len(os.listdir(screenshot_dir))

    return total