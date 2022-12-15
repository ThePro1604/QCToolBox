import os
import shutil
import PySimpleGUI as sg

def NameSwitcher(folder):
    Front = os.path.join(folder, "Front")
    Back = os.path.join(folder, "Back")
    os.mkdir(Front)
    os.mkdir(Back)

    for filename in os.listdir(folder):
        print(filename)
        if "page0" in filename.lower():
            shutil.move(folder + "/" + filename, Back + "/" + filename)
            new_name = filename[0:filename.lower().index("page")] + "page1" + filename[filename.lower().index("."):]
            os.rename(Back + "/" + filename, Back + "/" + new_name)

        elif "page1" in filename.lower():
            shutil.move(folder + "/" + filename, Front + "/" + filename)
            new_name = filename[0:filename.lower().index("page")] + "page0" + filename[filename.lower().index("."):]
            os.rename(Front + "/" + filename, Front + "/" + new_name)

    for filename in os.listdir(Back):
        shutil.move(Back + "/" + filename, folder + "/" + filename)

    for filename in os.listdir(Front):
        shutil.move(Front + "/" + filename, folder + "/" + filename)

    os.rmdir(Front)
    os.rmdir(Back)

    layout_popup = [
        [sg.Text("Done!")],
        [sg.Button('Close')]
    ]
    popup = sg.Window("Complete", layout_popup)

    while True:
        event, values = popup.read()
        if event == "Close" or event == sg.WIN_CLOSED:
            break
    popup.close()


top = [
    [sg.Text("Folder")],
    [sg.FolderBrowse(key="folder_name"), sg.InputText(key='myfolder')],
]

buttons = [
    [sg.Button('Start'), sg.Button('Close')],
]

copyright = [
    [sg.Text("Ⓒ By Shahaf Stossel", text_color="#A20909")],
]

description = [
    [sg.Text("Switch all the page0 and page1 in a folder ")],
]

layout = [
    [sg.Push(), sg.Column(description), sg.Push()],
    [sg.HSeparator()],
    [
        sg.Column(top, vertical_alignment="top", key='-COL1-'),
    ],
    [sg.Push(), sg.Column(buttons), sg.Push()],
    [sg.Push(), sg.Column(copyright), sg.Push()],
]

window = sg.Window("NameSwitcher", layout)

while True:
    event, values = window.read()
    if event == "Start":
        NameSwitcher(values['myfolder'])
    if event == sg.WIN_CLOSED or event == "Close":
        break

window.close()


