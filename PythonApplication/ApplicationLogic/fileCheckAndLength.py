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
    print("In no of files function")
    total = 0
    curr_dir = os.getcwd()

    screenshot_dir = curr_dir + "\Output\Screenshots"
    screenshot_len = len(os.listdir(screenshot_dir))
    audio_dir = curr_dir + "\Output\Audio"
    audio_len = len(os.listdir(audio_dir))
    print(screenshot_len,audio_len)
    if screenshot_len==audio_len:
        print('Exact number')
    elif screenshot_len+1==audio_len or screenshot_len==audio_len+1:
        print('one more')
    else:
        print('Different length')

    total=2*screenshot_len

    return total