# JOTE Note Summarizer for Meetings & Lectures
## Pre-requisites

1. Python version >= 3.9. [Click here to download python](https://www.python.org/downloads/)
2. Code editor of your choice ([VsCode](https://code.visualstudio.com/), [Spyder](https://www.spyder-ide.org/), ...)
3. Git will be needed if you want to clone the repository. [Click here to download git](https://git-scm.com/downloads)

## Generating the API keys
### How to generate the API keys for whisper module from replicate and chatgpt

#### Replicate API key

- To use the whisper module from replicate, you need to have a replicate account and a replicate API key.
- You can sign up for a free account on [https://replicate.com](https://replicate.com).
- Once you have an account, you can generate an API key by clicking on your profile in the top-right corner and selecting "View API keys" from the dropdown menu.
- Click on "Create new secret key" to generate a new key. You won't be able to view the key again, so store it somewhere safe.
- You can use the replicate API key to run the whisper model on replicate by setting the `REPLICATE_API_TOKEN` environment variable or modifying the variable in the main.py file. 

#### Chatgpt API key

- To use the chatgpt module, you need to have an OpenAI account and a chatgpt API key.
- You can sign up for an OpenAI account on [https://beta.openai.com](https://beta.openai.com).
- Once you have verified your account, you can generate an API key by logging in to your OpenAI account and visiting the API keys page.
- Click on your profile in the top-right corner and select "View API Key" to get your key.
- Click on "Create new secret key" to generate a new key. You won't be able to view the key again, so store it somewhere safe.
- You can use the chatgpt API key to access the chatgpt model on OpenAI by setting the `OPENAI_API_KEY` environment variable or creating a client with `openai.api_key = ...`.

## How to install tesseract OCR software in windows

### Download the installer

- The first step to install tesseract OCR for windows is to download the `.exe` installer that corresponds to your machine’s operating system.
- You can download the installer from [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki) or [https://digi.bib.uni-mannheim.de/tesseract/](https://digi.bib.uni-mannheim.de/tesseract/).
- Chances are, if you’re running any version of Windows later than Windows XP, you’re likely running Windows 64-bit on your machine⁴. If you are not sure, you can check your system type by following these steps:
    - Right-click on the Start button and select System.
    - Look for System type and see if it says 32-bit or 64-bit operating system.
    - Download the installer that matches your system type.

### Configure your installation

- Next, we’ll need to configure the tesseract installation.
- Run the installer and follow the instructions on the screen.
- Choose the installation path and language data to include. You can select multiple languages if you need to use tesseract for different languages.
- You can also choose to install additional components such as training tools, documentation, and command-line program.

### Add tesseract OCR to your environment variables

- To access tesseract-OCR from any location, you may have to add the directory where the tesseract-OCR binaries are located to the Path variables.
- The exact directory will depend on your installation path, but it is probably `C:\Program Files\Tesseract-OCR` or `C:\Program Files (x86)\Tesseract-OCR`.
- To add tesseract OCR to your environment variables, follow these steps:
    - Right-click on the Start button and select System.
    - Click on Advanced system settings on the left panel.
    - Click on Environment Variables at the bottom of the System Properties window.
    - Under System variables, find and select Path and click on Edit.
    - Click on New and type or paste the directory where tesseract-OCR is installed.
    - Click on OK to save the changes.

### Add tessdata_prefix to your environment variables

- To use tesseract with different language data, you may have to add another environment variable called `TESSDATA_PREFIX`.
- This variable should point to the directory where the language data files are located. By default, they are in a subdirectory called `tessdata` inside the installation directory.
- To add tessdata_prefix to your environment variables, follow these steps:
    - Right-click on the Start button and select System.
    - Click on Advanced system settings on the left panel.
    - Click on Environment Variables at the bottom of the System Properties window.
    - Under System variables, click on New and enter `TESSDATA_PREFIX` as the variable name and the directory where tessdata is located as the variable value. For example, `C:\Program Files\Tesseract-OCR\tessdata`.
    - Click on OK to save the changes.


## Setting up the application


* Clone the [repository](https://github.com/Sumedhbhat/MeetingSummarizer.git) or download the project in the form of a zip file and extract it
* Open the PythonApplication folder. Right-click and select Git Bash Here or open command prompt in the PythonApplication folder.
* This application needs many packages to be installed. You can do the same by using,
```
pip install -f requirements.txt
```

## Running the Application
- Once all the packages are installed, type
```
python main.py
```

If your system doesnot support CUDA or doesnot have NVIDIA GPU, you may get a warning. Please ignore this.
``` 
W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'cudart64_110.dll'; dlerror: cudart64_110.dll not found
I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
_tkinter.TclError: can't use "pyimage5" as iconphoto: not a photo image
```
- Click `Okay` on the disclaimer that informs about the data that we are collecting to generate the summary of the meeting or lecture
- Choose if you wish to consider the audio and video data to be included in the summary.
- If you wish to record the entire screen you can choose `Yes` on this dialog else you can choose `No`.
- Choose the screen which has the meeting from all the open screens.
- Unless you opt to record the whole screen, you will see a snipping tool that lets you crop the area of the screen you want to capture. After selecting the desired part, click on `Okay`.
- You can choose to `Pause`/`Play` capturing the data as you wish.
- Once the meeting is complete click on the `Stop` icon to start the summary generation.
- The final generated summary will then be made into a PDF file and saved in the `Downloads` folder. 


