import os
import fitz
import PySimpleGUI as sg


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
                        try:
                            doc = fitz.open(folder + "/" + nested_folder + "/" + nested_file)  # open document
                            i = 0
                            for page in doc:
                                if "page" in nested_file:
                                    name = nested_file[0:nested_file.lower().index("page")]
                                    pix = page.get_pixmap()  # render page to an image
                                    pix.save(f"{folder}/{nested_folder}/{name}page{i}.jpeg", 'JPEG')
                                    i += 1
                                if "supp" in nested_file:
                                    name = nested_file[0:nested_file.lower().index("supp")]
                                    pix = page.get_pixmap()  # render page to an image
                                    pix.save(f"{folder}/{nested_folder}/{name}supp{i}.jpeg", 'JPEG')
                                    i += 1
                            doc.close()
                            os.remove(folder + "/" + nested_folder + "/" + nested_file)
                        except:
                            continue

            elif ".pdf" in file:
                try:
                    doc = fitz.open(folder + "/" + file)  # open document
                    i = 0
                    for page in doc:
                        if "page" in file:
                            name = file[0:file.lower().index("page")]
                            pix = page.get_pixmap()  # render page to an image
                            pix.save(f"{folder}/{name}page{i}.jpeg", 'JPEG')
                            i += 1
                        if "supp" in file:
                            name = file[0:file.lower().index("supp")]
                            pix = page.get_pixmap()  # render page to an image
                            pix.save(f"{folder}/{name}supp{i}.jpeg", 'JPEG')
                            i += 1
                    doc.close()
                    os.remove(folder + "/" + file)
                except:
                    continue

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
        if event == "Start" and len(values['myfolder']) > 1:
            PDF2JPG(values['myfolder'])
        if event == sg.WIN_CLOSED or event == "Close":
            break

    window.close()


# python -m eel main.py web --onedir --noconsole -n=QCToolBox --icon="N:\Images\Shahaf\Tools\QCToolBox\web\assets\tabicon.png" --splash="N:\Images\Shahaf\Tools\QCToolBox\web\assets\loadingic
# on2.png" --hidden-import=pyi_splash