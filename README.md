# Hi there! My name is Andrew and this is Bass Transcriber repository.

Here you can see structure of the project and instruction to launch it on your own machine.

## Root directory

The root directory contains the system executable file, through which the application will be launched, as well as a file with a list of libraries, autotests and files related to Git and Docker.

## assets/ directory

The assets/ directory contains images for the web-page and files used to test the music recognition algorithm.

## pages/ directory

The pages/ directory contains files that will describe the front-end part of the application written in Streamlit. These files will be called via the main executable file in the root directory

## scripts/ directory

The scripts/ directory contains files responsible for the application logic. They describe the music recognition algorithm, the transcription function, a dictionary with notes markup and etc.

## Instruction

To launch the app clone this repository, install requierments.txt and launch command `streamlit run app.py`