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
    #print(os.getcwd())
    #os.chdir("../")
    #print(os.getcwd())
    curr_dir = os.getcwd()
    #audio_dir = curr_dir + "\Output\Audio"
    #total += len(os.listdir(audio_dir))

    screenshot_dir = curr_dir + "\Output\Screenshots"
    screenshot_len = len(os.listdir(screenshot_dir))

    audio_dir = curr_dir + "\Output\Audio"
    audio_len = len(os.listdir(audio_dir))
    if screenshot_len==audio_len:
        print('Exact number')
    elif screenshot_len+1==audio_len or screenshot_len==audio_len+1:
        print('one more')
    else: print('Not working')

    total=2*screenshot_len

    return total