import shutil
import PySimpleGUI as sg

<<<<<<< HEAD

def Duplicator(folder, file, num):
    # src = r'N:\Images\Shahaf\SupportBatch\TestJuan\16BE7530E9F84334B0E93C8DB3907AE5'
    # ext = r'_page0.jpeg'
    file = file.replace("\\", "/")
    suffix = file[file.rfind("_"):file.rfind(".")] + file[file.rfind("."):]

    print(file)

    # Change the 5 to what number you want to duplicate
    for i in range(int(num)):
        # shutil.copy(src + ext, f'{src +str(i) +  ext}')
        # shutil.copy(ext, f'{src[src.rfind("/"):ext.rfind("_p")] +str(i) +  suffix}')
        shutil.copy(file, folder + file[file.rfind("/"):file.rfind("_")] + str(i) + suffix)

    layout_popup = [
        [sg.Text("Done!")],
        [sg.Button('Close')]
    ]
    popup = sg.Window("Complete", layout_popup, background_color='#edfffd')

    while True:
        event, values = popup.read()
        if event == "Close" or event == sg.WIN_CLOSED:
            break
    popup.close()


left = [
    [sg.Text("Choose File")],
    [sg.FileBrowse(key="file_name", file_types=(("ALL Files", "*.*"),)), sg.InputText(key='myfile')],
]

right = [
    [sg.Text("Output Folder")],
    [sg.FolderBrowse(key="folder_name"), sg.InputText(key='myfolder')],
]

middle = [
    [sg.Text("Amount of Duplicates"), sg.InputText(key='num', size=(5, 1))],
]

buttons = [
    [sg.Button('Start'), sg.Button('Close')],
]

copyright = [
    [sg.Text("Ⓒ By Shahaf Stossel", text_color="#A20909")],
]

layout = [
    [
        sg.Column(left, vertical_alignment="top", key='-COL1-'),
        sg.VSeparator(),
        sg.Column(right, vertical_alignment="top", key='-COL1-')
    ],
    [sg.VPush()],
    [sg.Push(), sg.Column(middle), sg.Push()],
    [sg.VPush()],
    [sg.Push(), sg.Column(buttons), sg.Push()],
    [sg.Push(), sg.Column(copyright), sg.Push()],

]

window = sg.Window("Duplicator", layout)

# layout = [
#     [sg.Text("Output Folder")],
#     [sg.FolderBrowse(key="folder_name"), sg.InputText(key='myfolder')],
#     [sg.Text("Choose File")],
#     [sg.FileBrowse(key="file_name", file_types=(("ALL Files", "*.*"),)), sg.InputText(key='myfile')],
#     [sg.Text("Amount of Duplicates"), sg.InputText(key='num', size=(5, 1))],
#     [sg.Button('Start'), sg.Button('Close')],
#     [sg.Text("Ⓒ By Shahaf Stossel", text_color="#A20909")],
# ]

# window = sg.Window("Duplicator", layout)

while True:
    event, values = window.read()
    # if event == "file_name":
    #     values['myfile'] = values['file_name']
    if event == "Start":
        Duplicator(values['myfolder'], values['file_name'], values['num'])
    if event == sg.WIN_CLOSED or event == "Close":
        break

window.close()
=======
def ToolRun_Duplicator():
    def Duplicator(folder, file, num):
        # src = r'N:\Images\Shahaf\SupportBatch\TestJuan\16BE7530E9F84334B0E93C8DB3907AE5'
        # ext = r'_page0.jpeg'
        file = file.replace("\\", "/")
        suffix = file[file.rfind("_"):file.rfind(".")] + file[file.rfind("."):]

        print(file)

        # Change the 5 to what number you want to duplicate
        for i in range(int(num)):
            # shutil.copy(src + ext, f'{src +str(i) +  ext}')
            # shutil.copy(ext, f'{src[src.rfind("/"):ext.rfind("_p")] +str(i) +  suffix}')
            shutil.copy(file, folder + file[file.rfind("/"):file.rfind("_")] + str(i) + suffix)

        layout_popup = [
            [sg.Text("Done!")],
            [sg.Button('Close')]
        ]
        popup = sg.Window("Complete", layout_popup, background_color='#edfffd')

        while True:
            event, values = popup.read()
            if event == "Close" or event == sg.WIN_CLOSED:
                break
        popup.close()


    left = [
        [sg.Text("Choose File")],
        [sg.FileBrowse(key="file_name", file_types=(("ALL Files", "*.*"),)), sg.InputText(key='myfile')],
    ]

    right = [
        [sg.Text("Output Folder")],
        [sg.FolderBrowse(key="folder_name"), sg.InputText(key='myfolder')],
    ]

    middle = [
        [sg.Text("Amount of Duplicates"), sg.InputText(key='num', size=(5, 1))],
    ]

    buttons = [
        [sg.Button('Start'), sg.Button('Close')],
    ]

    copyright = [
        [sg.Text("Ⓒ By Shahaf Stossel", text_color="#A20909")],
    ]

    layout = [
        [
            sg.Column(left, vertical_alignment="top", key='-COL1-'),
            sg.VSeparator(),
            sg.Column(right, vertical_alignment="top", key='-COL1-')
        ],
        [sg.VPush()],
        [sg.Push(), sg.Column(middle), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Column(buttons), sg.Push()],
        [sg.Push(), sg.Column(copyright), sg.Push()],

    ]

    window = sg.Window("Duplicator", layout)

    # layout = [
    #     [sg.Text("Output Folder")],
    #     [sg.FolderBrowse(key="folder_name"), sg.InputText(key='myfolder')],
    #     [sg.Text("Choose File")],
    #     [sg.FileBrowse(key="file_name", file_types=(("ALL Files", "*.*"),)), sg.InputText(key='myfile')],
    #     [sg.Text("Amount of Duplicates"), sg.InputText(key='num', size=(5, 1))],
    #     [sg.Button('Start'), sg.Button('Close')],
    #     [sg.Text("Ⓒ By Shahaf Stossel", text_color="#A20909")],
    # ]

    # window = sg.Window("Duplicator", layout)

    while True:
        event, values = window.read()
        # if event == "file_name":
        #     values['myfile'] = values['file_name']
        if event == "Start":
            Duplicator(values['myfolder'], values['file_name'], values['num'])
        if event == sg.WIN_CLOSED or event == "Close":
            break

    window.close()
>>>>>>> 84b359e (Initial commit)
