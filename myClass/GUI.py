import PySimpleGUI as sg
from myClass.Editor import Editor

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
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    dir_src = values[0]
    dir_dst = values[1]
    e = Editor(dir_src, dir_dst)
    print(e)
window.close()

