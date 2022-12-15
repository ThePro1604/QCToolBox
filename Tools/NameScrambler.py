import os
import random
import string
import PySimpleGUI as sg

def ToolRun_scrambler():
    def scrambler(folder):
        # folder = r"N:\Images\Mamon\Bol\Bol_1\Front+Back"
        for count, filename in enumerate(os.listdir(folder)):
            num = random.randrange(0, 1000)
            letters = string.ascii_letters
            name = ''.join(random.choice(letters) for i in range(10))
            name += repr(num)
            dst = f"{str(name)}_page0.jpg"
            src = f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
            dst = f"{folder}/{dst}"

            os.rename(src, dst)

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
        [sg.Text("Scramble all the Images names in a specific folder")],
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


    window = sg.Window("NameScrambler", layout)

    while True:
        event, values = window.read()
        if event == "Start":
            scrambler(values['myfolder'])
        if event == sg.WIN_CLOSED or event == "Close":
            break

    window.close()

