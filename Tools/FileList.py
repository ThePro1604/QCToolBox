import os
import pandas as pd
import PySimpleGUI as sg


def ToolRun_FileList():
    #path of the file you want to enemurate
    def FileList(path):
        # path = "N:\Images\Mamon\Bol\DbRef\Bol_1"
        directory =[]
        filename=[]

        for (root,dirs, file) in os.walk(path):
            for f in file:
                directory.append(root)
                filename.append(f)
                print(f)

        #column name of the sheet
        df=pd.DataFrame(list(zip(directory,filename)),columns=['Directory',"filename"])
        #change the file of exccl sheet
        df.to_csv(path + "/all.csv")

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
        [sg.Text("Create an excel file from all the documents in a specific folder")],
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



    window = sg.Window("FileList", layout)

    while True:
        event, values = window.read()
        if event == "Start" and len(values['myfolder']) > 1:
            FileList(values['myfolder'])
        if event == sg.WIN_CLOSED or event == "Close":
            break

    window.close()
