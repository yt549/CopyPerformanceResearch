import PySimpleGUI as sg
from myClass import Editor
import sys
'''
Author: Yingkai Tan

users can input like:
Import python files from  = "/Users/tanyingkai/Desktop/Neeva/CopyFrom"
Export python files to  = "/Users/tanyingkai/Desktop/Neeva/CopyTo"
File type: python (can modify Editor.py to any specific type)
'''
# All the stuff inside your window.
layout = [  [sg.Text('This is the test for Neeva')],
            [sg.Text('Enter the directory of python files to copy from: '), sg.InputText()],
            [sg.Text('Enter the copy to directory: '), sg.InputText()],
            [sg.Text('File type to transfer (.py for example): '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Copy and Paste Machine', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    dir_src = values[0]
    dir_dst = values[1]
    file_type = values[2]
    try:
        # here, I use copy1_shutil_CopyFile because it is the fastest one
        e = Editor.copy1_shutil_CopyFile(dir_src, dir_dst, file_type)
        break
    except IOError as e:
        print("Unable to copy file. %s" % e)
        exit(1)
    except:
        print("Unexpected error:", sys.exc_info())
        exit(1)
window.close()
