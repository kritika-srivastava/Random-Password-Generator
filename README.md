# Random-Password-Generator
&nbsp;
## [![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/kritika-srivastava/Random-Password-Generator/blob/master/LICENSE)![Project Status](https://img.shields.io/badge/Project-Completed-orange)[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
## ![Python Badge](https://img.shields.io/badge/Python-3.5%7C3.6%7C3.7-success)
#### *Welcome to Random Password Generation’s documentation! Here I shall give an overview of all the things you need to know to get started with this project.*
&nbsp;

![](photos/Password%20Generator.gif)
&nbsp;

&nbsp;

*This project demonstrates a simple basic password generator with randomized passwords of varying length and type.*
&nbsp;


## Technical Stack
###### -PyQt5
###### -Qt Designer
###### -Anaconda
###### -Python Libraries
        - Random
        - String

&nbsp;


## Functions
#### *You can generate the following types of passwords:*
##### -Small Alphabets
##### -Capital Alphabets
##### -Mixed Alphabets
##### -Numbers
##### -Alphabets and Numbers
##### -Alphabets Numbers and Symbols
&nbsp;

You can get the source code at my [Github Page](https://github.com/kritika-srivastava/Random-Password-Generator)
&nbsp;

Although I have specified the maximum limit of words in the QtDesigner SpinBox as 300, you can change the value by opening the [UI file](https://github.com/kritika-srivastava/Random-Password-Generator/blob/master/MainWindow.ui) in the QtDesigner.
&nbsp;

As of now, this project runs on Python 3.x . Make sure that PyQt5 should be installed in any of your python distributions. To start the program with the GUI (assuming all dependencies installed) run the GUI.py file.
If everything worked so far, the GUI should open up and look like this:
&nbsp;

<img src="photos/Capture.PNG">
&nbsp;
  
In order to compile the file in an executable, open anaconda prompt and change the directory to the one that contains GUI.py file. Now type the following command :
``` 
pyinstaller.exe -y -F --distpath="." GUI.py
``` 
The precompiled exe file can be found in the release section of this repository.
&nbsp;

## References
#### -[GUI Application Detailed tutorial](https://www.learnpyqt.com/examples/simple-sales-tax-calculator/)
#### -[PyQt5 Menubar Tutorial](https://techwithtim.net/tutorials/pyqt5-tutorial/menubar/)


