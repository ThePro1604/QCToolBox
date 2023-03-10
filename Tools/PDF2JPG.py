import os
import fitz
import PySimpleGUI as sg

<<<<<<< HEAD

def PDF2JPG(folder):
    def get_list_of_json_files():
        list_of_files = os.listdir(folder)
        return list_of_files

    def get_list_of_json_files_nested(nested):
        list_of_files = os.listdir(folder + "\\" + nested)
        return list_of_files

    list_of_files = get_list_of_json_files()
    for file in list_of_files:
        print(file)
        if "." not in file:
            nested_folder = file
            list_of_files_nested = get_list_of_json_files_nested(file)
            for nested_file in list_of_files_nested:
                if ".pdf" in nested_file:
                    doc = fitz.open(folder + "/" + nested_folder + "/" + nested_file)  # open document
                    i = 0
                    for page in doc:
                        name = nested_file[0:nested_file.lower().index("page")]
                        pix = page.get_pixmap()  # render page to an image
                        pix.save(f"{folder}/{nested_folder}/{name}page{i}.jpg", 'JPEG')
                        i += 1
                    doc.close()
                    os.remove(folder + "/" + nested_folder + "/" + nested_file)

        elif ".pdf" in file:
            doc = fitz.open(folder + "/" + file)  # open document
            i = 0
            for page in doc:
                name = file[0:file.lower().index("page")]
                pix = page.get_pixmap()  # render page to an image
                pix.save(f"{folder}/{name}page{i}.jpg", 'JPEG')
                i += 1
            doc.close()
            os.remove(folder + "/" + file)

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
    [sg.Text("??? By Shahaf Stossel", text_color="#A20909")],
]

description = [
    [sg.Text("Converts all PDF files to JPEG files")],
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
window = sg.Window("PDF2JPG", layout)

while True:
    event, values = window.read()
    if event == "Start":
        PDF2JPG(values['myfolder'])
    if event == sg.WIN_CLOSED or event == "Close":
        break

window.close()
=======
def ToolRun_PDF2JPG():
    def PDF2JPG(folder):
        def get_list_of_json_files():
            list_of_files = os.listdir(folder)
            return list_of_files

        def get_list_of_json_files_nested(nested):
            list_of_files = os.listdir(folder + "\\" + nested)
            return list_of_files

        list_of_files = get_list_of_json_files()
        for file in list_of_files:
            print(file)
            if "." not in file:
                nested_folder = file
                list_of_files_nested = get_list_of_json_files_nested(file)
                for nested_file in list_of_files_nested:
                    if ".pdf" in nested_file:
                        doc = fitz.open(folder + "/" + nested_folder + "/" + nested_file)  # open document
                        i = 0
                        for page in doc:
                            name = nested_file[0:nested_file.lower().index("page")]
                            pix = page.get_pixmap()  # render page to an image
                            pix.save(f"{folder}/{nested_folder}/{name}page{i}.jpg", 'JPEG')
                            i += 1
                        doc.close()
                        os.remove(folder + "/" + nested_folder + "/" + nested_file)

            elif ".pdf" in file:
                doc = fitz.open(folder + "/" + file)  # open document
                i = 0
                for page in doc:
                    name = file[0:file.lower().index("page")]
                    pix = page.get_pixmap()  # render page to an image
                    pix.save(f"{folder}/{name}page{i}.jpg", 'JPEG')
                    i += 1
                doc.close()
                os.remove(folder + "/" + file)

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
        [sg.Text("??? By Shahaf Stossel", text_color="#A20909")],
    ]

    description = [
        [sg.Text("Converts all PDF files to JPEG files")],
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
    window = sg.Window("PDF2JPG", layout)

    while True:
        event, values = window.read()
        if event == "Start":
            PDF2JPG(values['myfolder'])
        if event == sg.WIN_CLOSED or event == "Close":
            break

    window.close()
>>>>>>> 84b359e (Initial commit)
